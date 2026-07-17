class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        if len(word) == 0:
            return True
        visited = set() 
        def find(temp, i, j):
            if temp == word:
                return True
            if (i < 0 or i >= row or j < 0 or j >= col 
                or (i, j) in visited 
                or len(temp) >= len(word) 
                or board[i][j] != word[len(temp)]):
                return False
            visited.add((i, j))
            temp += board[i][j]
            if (find(temp, i+1, j) or
                find(temp, i-1, j) or
                find(temp, i, j+1) or
                find(temp, i, j-1)):
                return True
            visited.remove((i, j))
            return False
        for i in range(row):
            for j in range(col):
                if find("", i, j):
                    return True
        return False