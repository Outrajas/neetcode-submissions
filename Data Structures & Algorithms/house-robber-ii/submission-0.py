class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(arr):
            prev2, prev1 = 0, 0
            for val in arr:
                curr = max(prev1, val + prev2)
                prev2, prev1 = prev1, curr
            return prev1
        
        return max(helper(nums[:-1]), helper(nums[1:]))