def repate(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            result = func(*args, **kwargs)
            print(result)
        return result
    return wrapper