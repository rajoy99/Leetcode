class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        def binarysearch(arr,target):
            
            low=0
            high=len(arr)-1
            
            while low<=high:
                mid=(low+high)//2
                
                if arr[mid]==target:
                    return mid
                elif arr[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return -1
        
        for i in matrix:
            if binarysearch(i,target)!=-1:
                return True
            
        return False
            
            
        