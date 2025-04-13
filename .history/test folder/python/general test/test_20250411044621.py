def base (x):
    def power (n):
        return x ** n
    return power


square = base(2)
print
