class Counter:
    def __init__(self, start, end):
        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num - 1

# Driver code
if __name__ == '__main__':
    a, b = 2, 5
    c1 = Counter(a, b)
    c2 = Counter(a, b)
    
    # Iteration without using iter()
    print("Print the range without iter():")
    for i in c1:
        print("Counting:", i)
    
    print("\nPrint the range using iter():")
    
    # Using iter()
    obj = iter(c2)
    try:
        while True:  # Iterate until StopIteration is raised
            print("Counting:", next(obj))
    except StopIteration:
        print("\nIteration completed.")
