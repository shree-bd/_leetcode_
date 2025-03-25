class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        r, c = rows-1, 0

        while r>= 0 and c< cols:
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                return True
        return False

 