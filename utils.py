import time
from blackfire import apm

def burn_cpu(secs):
    t0 = time.time()
    elapsed = 0
    while (elapsed < secs):
        for _ in range(1000):
            pass
        elapsed = time.time() - t0

def burn_io(secs):
    time.sleep(secs)

def monitor_me(func=None):
    def inner_func(func):
        def wrapper(*args, **kwargs):
            apm.start_transaction()
            try:
                return func(*args, **kwargs)
            finally:
                apm.stop_transaction()
        return wrapper

    if callable(func):
        return inner_func(func)
    else:
        return inner_func
