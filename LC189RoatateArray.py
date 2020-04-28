class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=nums
        
        for i in range(k):
            temp=a.pop()
            a=[temp]+a
            
        nums[:]=a
            
        
            
