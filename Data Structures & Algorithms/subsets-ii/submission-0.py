class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        curr = []
        
        def sub(i):
            if i == len(nums):
                ans.append(curr.copy())
                return
            
            curr.append(nums[i])
            sub(i + 1)
            curr.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            sub(i + 1)
        
        sub(0)
        return ans