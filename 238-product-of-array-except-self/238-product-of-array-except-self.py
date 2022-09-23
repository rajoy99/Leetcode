class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
    
        prefix=[1]+[0 for i in range(len(nums))]
        postfix=[0 for i in range(len(nums))]+[1]
        
        for i in range(1,len(nums)+1):
            prefix[i]=prefix[i-1]*nums[i-1]
            
        for i in range(len(nums)-1,-1,-1):
            postfix[i]=postfix[i+1]*nums[i]
            
        res=[]
        for i in range(len(nums)):
            res.append(prefix[i]*postfix[i+1])
            
        return res
            
            

        