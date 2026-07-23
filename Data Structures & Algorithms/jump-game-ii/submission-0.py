class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        j=n-1
        count=0
        while j>0:
            for i in range(j):
                if nums[i]+i>=j:
                    j=i  
                    count+=1
                    break
        return count               