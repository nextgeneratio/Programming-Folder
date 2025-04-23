def gen():
    for i in range(1000000):
        yield i
        print(i)

g = gen() 
for i in g:
    print(i)# Uses less memory than list