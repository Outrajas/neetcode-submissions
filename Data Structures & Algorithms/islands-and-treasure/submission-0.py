class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        dist = 0
        while q:
            dist += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 2147483647:
                        grid[ni][nj] = dist
                        q.append((ni, nj))