class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in visited or grid[i][j] == 0:
                return 0
            visited.add((i, j))
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, dfs(i, j))
        return max_area