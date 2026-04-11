class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows = set() 
        seen_cols = set()
        seen_boxes = set()
        for y in range(9):
            for x in range(9):
                if (y, board[y][x]) in seen_rows or (x,board[y][x]) in seen_cols \
                or (x//3, y//3,board[y][x]) in seen_boxes:
                    print((y, board[y][x]))
                    print((x,board[y][x]))
                    print((x//3, y//3,board[y][x]), end='\n\n')
                    return False
                if board[y][x] != '.':
                    seen_rows.add((y, board[y][x]))
                    seen_cols.add((x, board[y][x]))
                    seen_boxes.add((x//3, y//3, board[y][x]))
        return True