class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ls = list(range(len(nums) + 1))
        missing = list(set(ls).difference(set(nums)))
        return missing[0]