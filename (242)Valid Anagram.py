class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls1 = []
        ls2 = []
        for i in s:
            ls1.append(i)
        for j in t:
            ls2.append(j)
        ls1.sort()
        ls2.sort()
        if(ls1 == ls2): return True
        else: return False