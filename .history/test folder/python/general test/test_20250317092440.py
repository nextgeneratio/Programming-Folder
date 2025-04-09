def infinite_counter():
    count = 1
    while True:
        yield count
        count += 1

# Usage
counter = infinite_counter()
for _ in counter:
    print(next(counter)) 
