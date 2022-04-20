class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if(i == target):
                return nums.index(i)
                break
            if(i > target):
                return nums.index(i)
                break
            if(i == nums[-1]):
                return len(nums)