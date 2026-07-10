class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        for i in range(len(nums)-k+1):
            temp=list(sorted(set(nums[i:i+k])))
            ans.append(temp[-1])
            temp=[]
        return ans    
        