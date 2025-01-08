# >>>>>>>>>>>>>>>> BFS <<<<<<<<<<<<<<<<<
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        num_islands = 0

        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def bfs(r, c):
            queue = collections.deque()
            visited.add((r, c))  # Add the starting cell to visited
            queue.append((r, c))  # Add the starting cell to the queue

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    # Check if the neighbor is valid and unvisited land
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        visited.add((nr, nc))  # Mark as visited
                        queue.append((nr, nc))  # Add to queue for further traversal

        # Traverse the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:  # Found a new island
                    bfs(r, c)  # Perform BFS for the island
                    num_islands += 1  # Increment the island count

        return num_islands



# Time Complexity: O(m x n)
# Space Complexity: O(m + n)

# >>>>>>>>>>>>>>>> DFS <<<<<<<<<<<<<<<<<

#  class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0

#         rows, cols = len(grid), len(grid[0])
#         num_islands = 0

#         directions = [[0,1],[0,-1],[-1,0],[1,0]]

#         def dfs(r,c):
#             if (0<= r < rows) and (0 <= c < cols) and grid[r][c] == "1":
#                 # Msrk the current cell as visited
#                 grid[r][c] = '2'

#                 for dr, dc in directions:
#                     dfs(r + dr, c + dc)

#         # Traverse the grid
#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col] == '1':   # Found an island
#                     num_islands += 1
#                     dfs(row,col) # Perform DFS to mark the entire island


#         return num_islands


                
# Time Complexity: O(m x n)
# Space Complexity: O(m x n)