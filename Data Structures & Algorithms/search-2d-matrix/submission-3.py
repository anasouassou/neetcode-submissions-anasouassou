class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, ROWS*COLS - 1

        while left <= right:
            mid = (left + right) // 2

            row, column = mid // COLS, mid % COLS

            if matrix[row][column] > target:
                right = mid - 1
            elif matrix[row][column] < target:
                left = mid + 1
            else:
                return True
            print("hello")
            
        return False



