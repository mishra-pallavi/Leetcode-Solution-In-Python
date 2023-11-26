# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.



def twoSum(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(len(nums)):
        for j in range (i+1, n):
            if nums[i]+nums[j] == target:
                return {i,i+1}

nums = [2,7,11,15]
target = 9
response = twoSum(nums,target)
print(response)
# Output: [0,1]