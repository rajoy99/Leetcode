class Solution:
    
    def checker(self,arr):
        
        hashSet=set()
        
        for i in arr:
            if i!='.':
                if i in hashSet:
                    return False
                else:
                    hashSet.add(i)
            
        return True
        
        
        
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #Row Check 
        
        for i in board:
            if not self.checker(i):
                return False
            
        # Column Check
        
        for j in range(9):
            ar=[]
            for i in range(9):
                ar.append(board[i][j])
                if i==8:
                    if not self.checker(ar):
                        return False
                    
        # 3 X 3 Check
        for i in [0,3,6]:
            for j in [0,3,6]:
                square=[board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if not self.checker(square):
                    return False
            
                        
        
        return True
    
            
        
        
        