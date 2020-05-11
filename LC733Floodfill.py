class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        prevcolor=image[sr][sc]

        
        
        def dfs(board,i,j,prevcolor,newColor):
            
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]==newColor or board[i][j]!=prevcolor:
                return
            
            board[i][j]=newColor
            
            
            dfs(board,i+1,j,prevcolor,newColor)
            dfs(board,i,j+1,prevcolor,newColor)
            dfs(board,i-1,j,prevcolor,newColor)
            dfs(board,i,j-1,prevcolor,newColor)
            
        dfs(image,sr,sc,prevcolor,newColor)
        
        return image
        
        
