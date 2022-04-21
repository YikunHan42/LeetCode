class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ls = []
        for i in range(numRows):
            new = []
            for j in range(i + 1):
                if((j == 0) | (j == i)):
                    new.append(1)
                else:
                    num = ls[(i - 1)][(j - 1)] + ls[(i - 1)][j]
                    new.append(num)
            ls.append(new)
        return ls