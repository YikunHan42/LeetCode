class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minvalue = float('inf')
        for i in range(len(prices)):
            minvalue = min(minvalue, prices[i])
            maxp = max(maxp, prices[i] - minvalue)
        return maxp