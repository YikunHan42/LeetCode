class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        ls = []
        for i in range(len(s)):
            if(s[i].isspace()): 
                if(count != 0):
                    ls.append(count)
                    count = 0
            else:
                count += 1
                if(i == len(s) - 1):
                    ls.append(count)
        return ls[-1]