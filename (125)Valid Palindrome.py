class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = str.lower(s)
        if(s[::-1] == s): return True
        else: return False