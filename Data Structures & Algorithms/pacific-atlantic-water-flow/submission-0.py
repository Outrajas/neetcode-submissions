class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()
        
        def dfs(i, j, ocean):
            ocean.add((i, j))
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in ocean and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, ocean)
        
        for i in range(rows):
            dfs(i, 0, pac)
            dfs(i, cols - 1, atl)
        for j in range(cols):
            dfs(0, j, pac)
            dfs(rows - 1, j, atl)
        
        return list(pac & atl)