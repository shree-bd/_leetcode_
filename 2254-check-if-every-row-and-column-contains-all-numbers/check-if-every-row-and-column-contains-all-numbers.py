class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for i in range(n):
            rows, cols = set(), set()

            for j in range(n):
                rows.add(matrix[i][j])
                cols.add(matrix[j][i])

            if rows != set(range(1,n+1)) or cols != set(range(1,n+1)):
                return False
        return True

        