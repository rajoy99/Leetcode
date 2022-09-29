class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        hashSet={}
        key=0
        
        def dfs(board,i,j,keyval):
            
            m=len(board)
            n=len(board[0])
        
            if i<0 or j<0 or i>=m or j>=n or board[i][j]!=1:
                return 
            
            board[i][j]='%'
            hashSet[keyval]+=1
            
            dfs(board,i+1,j,keyval)
            dfs(board,i-1,j,keyval)
            dfs(board,i,j+1,keyval)
            dfs(board,i,j-1,keyval)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    hashSet[key]=0
                    dfs(grid,i,j,key)
                    key+=1
          
        lst=[v for v in hashSet.values()]
        
        
        return max(lst) if lst else 0
                    
        