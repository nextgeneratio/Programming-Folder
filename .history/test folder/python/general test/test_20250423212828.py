num = [int(i) for i in input("Enter numbers separated by space: ").split()]

def rotate(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k is greater than n
    return nums[-k:] + nums[:-k]

print("Original list:", num)
print("Rotated list:", rotate(num, 2))
