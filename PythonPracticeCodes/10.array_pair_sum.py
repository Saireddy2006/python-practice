def array_pair_sum(nums):
    nums.sort()
    total_sum = 0
    for i in range(0, len(nums), 2):
        total_sum += nums[i]
    return total_sum
nums = [1, 4, 3, 2]
result = array_pair_sum(nums)
print(result)  # Output: 4 (1 + 3)