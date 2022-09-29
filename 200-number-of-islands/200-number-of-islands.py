class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(board,i,j):
            
            m=len(board)
            n=len(board[0])
            
            if i<0 or i>=m or j<0 or j>=n or board[i][j]!='1':
                return 
            
            board[i][j]='@'
            
            dfs(board,i+1,j)
            dfs(board,i-1,j)
            dfs(board,i,j+1)
            dfs(board,i,j-1)
            
            
        count=0 
        
        newgrid=grid.copy()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if newgrid[i][j]=='1':
                    dfs(newgrid,i,j)
                    count+=1
                    
                    
        return count