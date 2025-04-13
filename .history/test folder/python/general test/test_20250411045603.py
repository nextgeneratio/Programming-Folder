def count_func():
    start_num = 0
    def count_one():
        return 0 + 1
    return count_one


print(count_func())
print(count_func())
