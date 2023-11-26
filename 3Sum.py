# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]


def threeSum(nums):
    lenght = len(nums)
    res = []
    nums.sort()
    
    for i in range(lenght-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i+1
        r = lenght-1
        
        while l < r:
            total =nums[i]+nums[l]+nums[r]
            if total < 0:
                l = l+1
            elif total > 0:
                r = r-1
            else:
                res.append([nums[i],nums[l],nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l=l+1
                while l < r and nums[r] == nums[r-1]:
                    r = r-1
                l=l+1
                r=r-1
    return res 

nums = [-1,0,1,2,-1,-4]
res = threeSum(nums)

