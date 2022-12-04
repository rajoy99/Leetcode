class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isvalid(arr):
            arr=[v for v in arr if v!='.']
            return len(arr)==len(set(arr))
        
        for i in board:
            if not isvalid(i):
                return False
        board_T=[[0 for i in range(len(board))]for i in range(len(board))]
        
        for i in range(9):
            for j in range(9):
                board_T[i][j]=board[j][i]
             
        for i in board_T:
            if not isvalid(i):
                return False
            
        for i in [0,3,6]:
            for j in [0,3,6]:
                grid3X3=[board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if not isvalid(grid3X3):
                    return False
                
        return True
            
          
        