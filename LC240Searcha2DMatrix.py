class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def bins(arr,start,end,t):
            
            while start<=end:
                mid=(start+end)//2
                
                if arr[mid]==t:
                    return True
                elif arr[mid]>t:
                    end=mid-1
                else:
                    start=mid+1
            return False
        
        for i in matrix:
            if bins(i,0,len(i)-1,target)==True:
                return True
            
        return False
        
        
