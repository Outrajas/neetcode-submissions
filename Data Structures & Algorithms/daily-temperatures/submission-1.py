class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        hottest = 0
        for i in range(n - 1, -1, -1):
            if temperatures[i] >= hottest:
                hottest = temperatures[i]
                continue
            days = 1
            while temperatures[i + days] <= temperatures[i]:
                days += ans[i + days]
            ans[i] = days
        return ans