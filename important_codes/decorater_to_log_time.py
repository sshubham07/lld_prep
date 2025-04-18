import time

def check_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print(f"Total time = {t2 - t1:.2f} seconds")
    return wrapper

@check_time
def calc():
    time.sleep(10)
    print("Running calc method")

calc()
