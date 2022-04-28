class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        count = 0
        for j in dic.values():
            if(j % 2 == 1):
                count += 1
        if(count > 1): return False
        else: return True