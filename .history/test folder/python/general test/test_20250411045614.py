def count_func():
    start_num = 0
    def count_one():
        return start_num
    return count_one


print(count_func())
print(count_func())
