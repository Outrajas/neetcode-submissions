class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        col, d1, d2 = set(), set(), set()
        
        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            for c in range(n):
                if c not in col and (r - c) not in d1 and (r + c) not in d2:
                    board[r][c] = 'Q'
                    col.add(c); d1.add(r - c); d2.add(r + c)
                    dfs(r + 1)
                    board[r][c] = '.'
                    col.remove(c); d1.remove(r - c); d2.remove(r + c)
        
        dfs(0)
        return res