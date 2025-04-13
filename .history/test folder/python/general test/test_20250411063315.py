import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Time taken: {end - start}")
    return wrapper

@timer
def slow():
    time.sleep(1)
    print("Done!")

slow()
