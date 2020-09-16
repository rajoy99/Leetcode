class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        
        
        """
        mark1=set()
        mark2=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    mark1.add(i)
                    mark2.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in mark1:
                    matrix[i][j]=0
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j in mark2:
                    matrix[i][j]=0
        print(mark1,mark2)
