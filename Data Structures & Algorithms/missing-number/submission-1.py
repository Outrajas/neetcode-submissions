class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_all=0
        for i in range(len(nums)+1):
            xor_all^=i
        for i in nums:
            xor_all^=i
        return xor_all        