# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.


class Solution:
    def runningSum(self, nums):
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums


solution_instance = Solution()
n_value = [1,1,1,1,1]
result = solution_instance.runningSum(n_value)
print(result)

# [1,3,6,10]