class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l,r=0,len(numbers)-1
        
        while l<len(numbers) and r>0:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]>target:
                r=r-1
            else:
                l+=1
        
        