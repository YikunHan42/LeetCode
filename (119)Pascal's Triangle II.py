class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ls = []
        prev = []
        for i in range(rowIndex + 1):
            new = []
            for j in range(i + 1):
                if((j == 0) | (j == i)):
                    new.append(1)
                else:
                    num = prev[j - 1] + prev[j]
                    new.append(num)
            prev[:] = new
        return new