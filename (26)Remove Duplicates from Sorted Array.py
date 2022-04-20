class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ls = []
        for i in nums:
            if i not in ls:
                ls.append(i)
        for i in range(len(ls)):
            nums[i] = ls[i]
        return len(ls)