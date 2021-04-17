class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        count=0
        m,n=len(grid),len(grid[0])
        
        def dfs(grid,i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]!='1':
                return 
            
            grid[i][j]='$'
            
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    dfs(grid,i,j)
                    count+=1 
                    
        return count 
            
       