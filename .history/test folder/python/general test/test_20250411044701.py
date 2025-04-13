def power_func (x):
    def power (n):
        return x ** n
    return power


square = power_func(2)
print(square(2))  # Output: 4
