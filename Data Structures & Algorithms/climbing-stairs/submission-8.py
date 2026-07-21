class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def coun(curr):
            if curr == n:
                return 1
            if curr > n:
                return 0
            if curr in memo:
                return memo[curr]
            memo[curr] = coun(curr + 1) + coun(curr + 2)
            return memo[curr]
        
        return coun(0)