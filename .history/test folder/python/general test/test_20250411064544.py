def repate(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            result = func(*args, **kwargs)
        return result
    return wrapper


@repate
def laugh():
    print("")
