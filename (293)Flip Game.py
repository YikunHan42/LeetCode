class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        ls = []
        new = []
        if(len(currentState) <= 1): return []
        for i in range(len(currentState) - 1):
            new = list(currentState)
            if((currentState[i] == "+") & (currentState[i + 1] == "+")):
               new[i] = "-"
               new[i + 1] = "-"
               new = ''.join(new)
               ls.append(new)
        return ls