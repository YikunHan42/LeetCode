class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxarea = min(height[i], height[j]) * j
        while(i < j):
            if(height[i] <= height[j]):
                i += 1
                new = min(height[i], height[j]) * (j - i)
                maxarea = max(maxarea, new)
            else:
                j -= 1
                new = min(height[i], height[j]) * (j - i)
                maxarea = max(maxarea, new) 
        return maxarea