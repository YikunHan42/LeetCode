class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1): return 1
        elif(n == 2): return 2
        ls = []
        ls.append(1)
        ls.append(2)
        for i in range(2, n):
            num = ls[i - 2] + ls[i - 1]
            ls.append(num)
        return ls[-1]