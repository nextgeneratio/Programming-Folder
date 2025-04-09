def infinite_counter():
    count = 1
    while True:
        yield count
        count += 1

# Usage
counter = infinite_counter()
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
