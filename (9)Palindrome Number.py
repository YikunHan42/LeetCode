class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if(len(x) == 1): return True
        for i in range(int(len(x)/2)):
            if(x[i] != x[(len(x) - i- 1)]):
               return False
               break
            if(i == int(len(x)/2) - 1): return True