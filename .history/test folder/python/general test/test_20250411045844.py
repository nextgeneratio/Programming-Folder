def count_func():
    start_num = 0

    def count_one():
        start_num += 1
        return start_num

    return count_one


counter = count_func()
print(counter())  # Output: 1
print(counter())  # Output: 2
print(counter())  # Output: 3
