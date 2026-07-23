class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]
        
        def dfs(i, j):
            if memo[i][j]:
                return memo[i][j]
            max_path = 1
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > matrix[i][j]:
                    max_path = max(max_path, 1 + dfs(ni, nj))
            memo[i][j] = max_path
            return max_path
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j))
        return ans