def repate(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper