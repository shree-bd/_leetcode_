class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0




# BRUTE FORCE SOLUTION

        """
        ROWS, COLS = len(matrix), len(matrix[0])
        copy = [[matrix[i][j] for j in range(COLS)] for i in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    for k in range(COLS):
                        copy[i][k] = 0
                    for k in range(ROWS):
                        copy[k][j] = 0

        for i in range(ROWS):
            for j in range(COLS):
                matrix[i][j] = copy[i][j]
        
# Time Complexity: O(M*N)
# Space Complexity: O(M*N)

"""