class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        max_area = 0

        def dfs(r,c):
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r,c) in visited):
                return 0

            # MARK THE CALL ARE VISITED
            visited.add((r,c))

            # RETURN THE AREA OF THE CURRENT ISLAND
            return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))

 
        for r in range(rows):
            for c in range(cols):
                # Only start DFS if the cell is land and hasn't been visited
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))  # Track the maximum area

        return max_area
        