class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def helper(nums,l,r,target):
            
            if l<=r:
                mid=(l+r)//2

                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    return helper(nums,l,mid-1,target)
                else:
                    return helper(nums,mid+1,r,target)
            else:
                return -1

                    
        return helper(nums,0,len(nums)-1,target)