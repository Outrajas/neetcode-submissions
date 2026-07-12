class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1]>nums[0]:
           return nums[0]
        r=0
        l=len(nums)-1
        if l==0:
            return nums[0]
        while r<l:
            if nums[r+1]<nums[r]:
                return nums[r+1]
            if  nums[l-1]>nums[l]:
                return nums[l]
            r+=1
            l-=1    
        return min(l,r+1)   
           