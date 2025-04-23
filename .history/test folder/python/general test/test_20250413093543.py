def gen():
    for i in range(1000000):
        yield i
        print(i)

g = gen() 
for i in g:
    pri# Uses less memory than list