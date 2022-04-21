class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        max = sum
        for i in range(1, len(nums)):
            if((sum + nums[i]) >= nums[i]): sum += nums[i]
            if((sum + nums[i]) < nums[i]): sum = nums[i]
            if(sum > max): max = sum
        return max