"""F005 bounded model: async ordering and cleanup/error propagation.

This is CPython asyncio model evidence, not Dart runtime validation.
"""
import asyncio
import platform
import sys


async def ordering_case():
    trace = []
    loop = asyncio.get_running_loop()
    loop.call_later(0, trace.append, "timer_event")
    loop.call_soon(trace.append, "ready_callback")
    await asyncio.sleep(0)
    trace.append("after_yield")
    await asyncio.sleep(0.001)
    return trace


async def unsafe_resource_case():
    state = {"open": False}
    trace = []
    try:
        state["open"] = True
        trace.append("opened")
        await asyncio.sleep(0)
        raise RuntimeError("modeled failure")
    except RuntimeError:
        trace.append("error_observed")
        # Deliberately missing cleanup.
    return state, trace


async def finally_cleanup_case():
    state = {"open": False}
    trace = []
    try:
        state["open"] = True
        trace.append("opened")
        await asyncio.sleep(0)
        raise RuntimeError("modeled failure")
    except RuntimeError:
        trace.append("error_observed")
    finally:
        state["open"] = False
        trace.append("closed")
    return state, trace


async def main():
    ordering = await ordering_case()
    unsafe_state, unsafe_trace = await unsafe_resource_case()
    safe_state, safe_trace = await finally_cleanup_case()

    assert "ready_callback" in ordering
    assert "timer_event" in ordering
    assert unsafe_state["open"] is True
    assert safe_state["open"] is False
    assert safe_trace[-1] == "closed"

    print("python", sys.version.split()[0], "platform", platform.platform())
    print("ordering", ordering)
    print("unsafe_cleanup", unsafe_state, unsafe_trace)
    print("finally_cleanup", safe_state, safe_trace)


if __name__ == "__main__":
    asyncio.run(main())
