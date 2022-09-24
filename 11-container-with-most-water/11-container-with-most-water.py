class Solution:
    def maxArea(self, height: List[int]) -> int:
            
        if len(height)==0 or len(height)==1:
            return 0

        maxsofar=-math.inf

        l,r=0,len(height)-1
        
        while l<r:
            area=min(height[l],height[r])*(r-l)
            maxsofar=max(maxsofar,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
                
        return maxsofar
                
            