class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0
        i,curr=0,len(heights)-1
        while i<=curr: 
            area=(curr-i)* min(heights[curr],heights[i])
            ans=max(ans,area)
            if heights[i]<heights[curr]:
                i+=1 
                continue
            curr-=1            
        return ans  