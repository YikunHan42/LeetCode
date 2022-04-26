class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        length = len(columnTitle)
        weight = pow(26, length - 1)
        sum = 0
        for i in columnTitle:
            sum += weight * (ord(i) - 64)
            weight /= 26
        return int(sum)