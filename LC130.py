class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board,i,j):
            
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!='O':
                return
            board[i][j]='@'
            
            dfs(board,i-1,j)
            dfs(board,i+1,j)
            dfs(board,i,j-1)
            dfs(board,i,j+1)
          
        m=len(board)
        if m==0:
            return
        n=len(board[0])
        if n==0:
            return 
       
        for j in range(n):
            if board[0][j]=='O':
                dfs(board,0,j)
            if board[m-1][j]=='O':
                dfs(board,m-1,j)
                        
        for i in range(m):
            if board[i][0]=='O':
                dfs(board,i,0)
            if board[i][n-1]=='O':
                dfs(board,i,n-1)
                
                
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
        for i in range(m):
            for j in range(n):
                if board[i][j]=='@':
                    board[i][j]='O'
