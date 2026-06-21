class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWs, COLs = len(matrix), len(matrix[0])
        N = ROWs*COLs

        left, right = 0, N - 1

        while left <= right:

            middle = left + (right - left)//2

            row, col = middle // COLs, middle % COLs

            print("middle:", middle, "row:", row, "col:", col)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = middle - 1
            else: 
                left = middle + 1

        return False