class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        new = columnNumber
        length = 0
        weight = 1
        while(new > 0):
            new -= pow(26, weight)
            weight += 1
            length += 1
        out = ""
        for i in range(length):
            if(columnNumber > 26):
                num = int((columnNumber - 1) / pow(26, length - i - 1))
            else:
                num = int(columnNumber / pow(26, length - i - 1))
            a = chr(num + 64)
            out += a
            columnNumber -= num * pow(26, length - i - 1)
        return out