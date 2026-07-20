class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return
            board[i][j] = 'S'
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(i + di, j + dj)
        
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'