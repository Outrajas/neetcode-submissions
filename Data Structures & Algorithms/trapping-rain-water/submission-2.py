class Solution:
    def trap(self, heights: List[int]) -> int:
        ans = 0
        i, curr = 0, len(heights) - 1
        maxL, maxR = heights[i], heights[curr]
        while i < curr:
            if maxL < maxR:
                i += 1
                maxL = max(maxL, heights[i])
                ans += maxL - heights[i]
            else:
                curr -= 1
                maxR = max(maxR, heights[curr])
                ans += maxR - heights[curr]
        return ans