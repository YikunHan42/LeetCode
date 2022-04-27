class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ls1 = []
        ls2 = []
        for i in range(len(wordsDict)):
            if(wordsDict[i] == word1):
                ls1.append(i)
        for j in range(len(wordsDict)):
            if(wordsDict[j] == word2):
                ls2.append(j)
        ls = []
        mindis = float('inf')
        for i in ls1:
            for j in ls2:
                diff = abs(i - j)
                mindis = min(mindis, diff)
        return int(mindis)