class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [x for x in board[i] if x != '.']
            if len(row) != len(set(row)):
                return False
            col = [board[j][i] for j in range(9) if board[j][i] != '.']
            if len(col) != len(set(col)):
                return False

        for k in range(0, 9, 3):
            for h in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        if board[k+i][h+j] != '.':
                            box.append(board[k+i][h+j])
                if len(box) != len(set(box)):
                    return False
        return True