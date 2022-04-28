class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        ls1 = ['0', '1', '8']
        ls2 = ['6', '9']
        length = len(num)
        ls = []
        for i in num[::-1]:
            if i in ls1: ls.append(i)
            elif i in ls2:
                if(i == '6'): ls.append('9')
                if(i == '9'): ls.append('6')
            else: 
                return False  
        new = ''.join(ls)
        if(new == num): return True
        else: return False