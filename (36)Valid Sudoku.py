class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            lsrow = []
            for j in range(9):
                if(board[i][j].isnumeric()):
                    if(board[i][j] not in lsrow):
                        lsrow.append(board[i][j])
                    else: 
                        return False
        for i in range(9):
            lscolumn = []
            for j in range(9):
                if(board[j][i].isnumeric()):
                    if(board[j][i] not in lscolumn):
                        lscolumn.append(board[j][i])
                    else: 
                        return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
               lsnine = []
               lsnine.append(board[i][j])
               lsnine.append(board[i + 1][j])
               lsnine.append(board[i + 2][j])
               lsnine.append(board[i][j + 1])
               lsnine.append(board[i + 1][j + 1])
               lsnine.append(board[i + 2][j + 1])
               lsnine.append(board[i][j + 2])
               lsnine.append(board[i + 1][j + 2])
               lsnine.append(board[i + 2][j + 2])
               while('.' in lsnine):
                    lsnine.remove('.')
               if(len(set(lsnine)) != len(lsnine)): 
                    return False
        return True
               
               