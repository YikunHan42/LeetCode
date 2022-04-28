class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for item in s:
            dic[item] = dic.get(item, 0) + 1
        count = 0
        for i in dic.keys():
            if(dic[i] == 1): 
                count += 1 
                break
        if(count == 0): return -1
        else:
            for j in range(len(s)):
                if(s[j] == i): return j