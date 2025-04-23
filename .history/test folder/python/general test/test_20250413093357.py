def gen():
    for i in range(1000000):
        yield i
        print(i)

g = gen()  # Uses less memory than list
print(g)  # <generator object gen at 0x7f8c1c0e5d60>