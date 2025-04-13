import time

def delay(n):
    def inner(func):
        def wrapper(*args, **kwargs):
            time.sleep(n)
            return func(*args, **kwargs)
        return wrapper
    return inner

@delay(2)
def 
