def gen():
    for i in range(1000000):
        yield i

g = gen()  # Uses less memory than list
print