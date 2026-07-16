class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for p in points:
            dist = (p[0]**2 + p[1]**2)**0.5
            ans.append((dist, p))
        ans.sort(key=lambda x: x[0])
        return [p for _, p in ans[:k]]