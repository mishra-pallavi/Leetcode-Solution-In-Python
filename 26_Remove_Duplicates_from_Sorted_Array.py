class Solution:
    def removeDuplicates(self, nums):
        j = 1
        for i in range(1,len(nums)):
            if(nums[i] != nums[i-1]):
                nums[j] = nums[i]
                j += 1
        return j

solution_instance = Solution()
n_value = [1,1,2]
result = solution_instance.removeDuplicates(n_value)
print(result)


# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]