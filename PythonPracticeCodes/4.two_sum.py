from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
        if target - nums[i] in dic:
            return [dic[target - nums[i]], i]
        dic[nums[i]] = i
    return []
 


# Define nums and target
nums = [2, 7, 11, 15]
target = 9

# Call the function
result = two_sum(nums, target)
print(result)  # Output: [0, 1]