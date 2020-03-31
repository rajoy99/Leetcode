class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        
        for i in range(len(intervals)-1):
            a=intervals[i]
            b=intervals[i+1]
            
            if a[1]>=b[0]:
                b[1]=max(a[1],b[1])
                b[0]=min(a[0],b[0])
                intervals[i]='@'
        new=[]
        for i in intervals:
            if i!='@':
                new.append(i)
                
        return new 
