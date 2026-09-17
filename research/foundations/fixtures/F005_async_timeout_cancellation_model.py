"""F005 bounded comparison model: timeout of a waiter vs cancellation of work.

This is CPython asyncio evidence, not Dart runtime evidence.
"""
import asyncio
import platform
import sys


async def underlying(log):
    log.append("started")
    await asyncio.sleep(0.05)
    log.append("side_effect")
    return "done"


async def timeout_only():
    log = []
    task = asyncio.create_task(underlying(log))
    try:
        # shield makes the boundary explicit: this waiter times out without
        # cancelling the underlying task.
        await asyncio.wait_for(asyncio.shield(task), timeout=0.01)
    except TimeoutError:
        log.append("caller_timeout")
    await task
    return log


async def cooperative_cancellation():
    log = []
    cancel = asyncio.Event()

    async def operation():
        log.append("started")
        for _ in range(10):
            if cancel.is_set():
                log.append("cancel_observed")
                return "cancelled"
            await asyncio.sleep(0.005)
        log.append("side_effect")
        return "done"

    task = asyncio.create_task(operation())
    await asyncio.sleep(0.01)
    cancel.set()
    result = await task
    return log, result


async def main():
    timeout_log = await timeout_only()
    cancel_log, cancel_result = await cooperative_cancellation()

    print("python", sys.version.split()[0], "platform", platform.platform())
    print("timeout_only", timeout_log)
    print("cooperative", (cancel_log, cancel_result))

    assert timeout_log == ["started", "caller_timeout", "side_effect"]
    assert cancel_log == ["started", "cancel_observed"]
    assert cancel_result == "cancelled"
    print("PASS")


if __name__ == "__main__":
    asyncio.run(main())
