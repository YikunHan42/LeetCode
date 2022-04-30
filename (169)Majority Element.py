class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        for j in dic.keys():
            if(dic[j] > (len(nums)/2)): return j