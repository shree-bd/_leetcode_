# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>in O(1) space complexity<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if r == rows-1 and c == cols-1:
                    continue # skip bottom right corner
                elif r == rows-1:
                    grid[r][c] += grid[r][c+1] # last rows
                elif c == cols-1:
                    grid[r][c] += grid[r+1][c] # last column
                else:
                    grid[r][c] += min(grid[r+1][c], grid[r][c+1]) #choose min path
        return grid[0][0]

# Time Complexity: O(M*N)
# Space Complexity: O(1)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>reservoir sampling<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = [[float("inf")] * (cols+1) for r in range(rows+1)]
        res[rows-1][cols] = 0

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r+1][c], res[r][c+1])
        return res[0][0]

# Time Complexity: O(M*N)
# Space Complexity: O(M*n)
"""