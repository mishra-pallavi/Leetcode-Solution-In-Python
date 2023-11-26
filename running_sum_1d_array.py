# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def running_sum(nums):
    respone = [0] * len(nums)
    respone[0] = nums[0]
    for n in range(1, len(nums)):
        respone[n] = respone[n-1]+nums[n]
    return respone

nums = [1,2,3,4]
respone = running_sum(nums)
print(respone)
