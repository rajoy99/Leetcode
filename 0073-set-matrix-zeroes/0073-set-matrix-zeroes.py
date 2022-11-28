class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x0,y0=set(),set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    x0.add(i)
                    y0.add(j)
                    
        for i in list(x0):
            for j in range(len(matrix[0])):
                matrix[i][j]=0
                    
        for i in range(len(matrix)):
            for j in list(y0):
                matrix[i][j]=0
                    
                    
                    
