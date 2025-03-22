class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
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