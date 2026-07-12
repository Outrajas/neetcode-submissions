class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) >> 1
            total = 0
            for p in piles:
                total += (p + mid - 1) // mid
                if total > h:
                    break
            if total > h:
                l = mid + 1
            else:
                r = mid
        return l