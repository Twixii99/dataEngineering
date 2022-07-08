def find_max(nums):
    max_number = -10**9

    for num in nums:
        if num > max_number:
            max_number = num
    return max_number

def find_max_simple(nums):
    return max(nums)

print(find_max([4, 6, 8, 24, 12, 2]))
print(find_max_simple([4, 6, 8, 24, 12, 2]))