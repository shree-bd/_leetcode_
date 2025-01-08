class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        directions = [[0,1],[0,-1],[-1,0],[1,0]]

        def dfs(grid, r,c):
            if (0<= r < rows) and (0 <= c < cols) and grid[r][c] == "1":
                grid[r][c] = '0'

                for row_inc, col_inc in directions:
                    dfs(grid, r + row_inc, c + col_inc)


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    num_islands += 1
                    dfs(grid, row,col)


        return num_islands


                
        