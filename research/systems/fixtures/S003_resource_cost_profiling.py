import json
import time
import tracemalloc


def measure(label, fn):
    tracemalloc.start()
    start_current, _ = tracemalloc.get_traced_memory()
    wall_start = time.perf_counter_ns()
    cpu_start = time.process_time_ns()

    result = fn()

    cpu_end = time.process_time_ns()
    wall_end = time.perf_counter_ns()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {
        "label": label,
        "result": result,
        "wall_ms": (wall_end - wall_start) / 1e6,
        "cpu_ms": (cpu_end - cpu_start) / 1e6,
        "peak_python_kib": peak / 1024,
        "net_python_kib": (current - start_current) / 1024,
    }


def cpu_work():
    return sum(i * i for i in range(900_000))


def wait_work():
    time.sleep(0.08)
    return 1


def memory_work():
    blocks = [bytearray(1024) for _ in range(5000)]
    return sum(len(block) for block in blocks)


rows = [
    measure("cpu_work", cpu_work),
    measure("wait_work", wait_work),
    measure("memory_work", memory_work),
]
print(json.dumps(rows, indent=2))

# Bounded semantic/resource oracles. These are intentionally broad enough to
# distinguish the workload classes without pretending to define portable
# performance thresholds.
assert rows[1]["wall_ms"] >= 70
assert rows[1]["cpu_ms"] < rows[1]["wall_ms"] / 4
assert rows[2]["peak_python_kib"] > 4000
assert rows[0]["cpu_ms"] > rows[1]["cpu_ms"] * 5
