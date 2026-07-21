class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        ans = 0
        
        while heap:
            t, i, j = heapq.heappop(heap)
            ans = max(ans, t)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if i == n - 1 and j == n - 1:
                return ans
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                    heapq.heappush(heap, (grid[ni][nj], ni, nj))
        return ans