class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        directions = [[0,1],[0,-1],[-1,0],[1,0]]

        def dfs(r,c):
            if (0<= r < rows) and (0 <= c < cols) and grid[r][c] == "1":
                # Msrk the current cell as visited
                grid[r][c] = '2'

                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        # Traverse the grid
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':   # Found an island
                    num_islands += 1
                    dfs(row,col) # Perform DFS to mark the entire island


        return num_islands


                
        