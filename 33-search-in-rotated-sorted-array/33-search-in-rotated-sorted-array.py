class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        pivot=0
        
        for k in range(1,len(nums)):
            if nums[k]<nums[k-1]:
                pivot=k
                break
                
        print("pvt",pivot)
        
        
        originalArray=nums[pivot:]+nums[:pivot]
        
        def binarysearch(arr,target):
            
            lo=0
            hi=len(arr)-1
            
            while lo<=hi:
                
                mid=(lo+hi)//2
                
                if arr[mid]==target:
                    return mid
                elif arr[mid]>target:
                    hi=mid-1
                else:
                    lo=mid+1
                    
            return -1     
        
        res=binarysearch(originalArray,target)
        
        return (res+pivot)%len(nums) if res!=-1 else res
                