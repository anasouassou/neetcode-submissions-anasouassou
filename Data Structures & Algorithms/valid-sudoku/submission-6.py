class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows, seen_cols, seen_boxes = set(), set(), set()

        for i in range(9):
            for j in range(9):
                print((i, board[i][j]) in seen_rows)
                print((j, board[i][j]) in seen_cols)
                print(((i//3, j//3), board[i][j]) in seen_boxes)
                if (i, board[i][j]) in seen_rows or (j, board[i][j]) in seen_cols or ((i//3, j//3), board[i][j]) in seen_boxes:
                    print(seen_rows, ' ', seen_cols, ' ', seen_boxes)
                    print((i, board[i][j]))
                    print((i,board[i][j]))
                    print((i//3,j//3,board[i][j]))
                    return False
                if board[i][j] != '.':
                    seen_rows.add((i, board[i][j]))
                    seen_cols.add((j, board[i][j]))
                    seen_boxes.add(((i//3, j//3), board[i][j]))
            
        return True