class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = {}
        ele = []
        ans = []
        t1 = [(0 - x) for x in nums]
        for i, num in enumerate(nums):
            seen = {}
            targ = t1[i]
            for j in range(i + 1, len(nums)):
                diff = targ - nums[j]
                if diff in seen:
                    ele = [num, diff, nums[j]]
                    ele.sort()
                    if ele not in ans:
                        ans.append(ele)
                seen[nums[j]] = j
        return ans