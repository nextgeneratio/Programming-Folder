num = [int(i) for i in input("Enter numbers separated by space: ").split()]

def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate if nums.count(candidate) > len(nums) // 2 else None

pri
