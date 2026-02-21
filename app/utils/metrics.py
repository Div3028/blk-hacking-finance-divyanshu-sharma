import psutil
import threading

LAST_EXECUTION_TIME = 0

def set_last_execution_time(duration):
    global LAST_EXECUTION_TIME
    LAST_EXECUTION_TIME = duration

def performance_report():
    process = psutil.Process()
    return {
        "time": f"{LAST_EXECUTION_TIME:.2f} ms",
        "memory": f"{process.memory_info().rss / 1024**2:.2f} MB",
        "threads": threading.active_count()
    }