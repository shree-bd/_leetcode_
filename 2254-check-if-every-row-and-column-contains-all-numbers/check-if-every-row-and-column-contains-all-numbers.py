class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        # check each row
        for row in matrix:
            if set(row) != set(range(1,n+1)):
                return False

        # check each column
        for col in range(n):
            if set(matrix[row][col] for row in range(n)) != set(range(1,n+1)):
                return False

        return True

        
# class Solution:
#     def checkValid(self, matrix: List[List[int]]) -> bool:
#         n = len(matrix)
#         for row, col in zip(matrix, zip(*matrix)):
#             if len(set(row)) != n or len(set(col)) != n:
#                 return False
#         return True