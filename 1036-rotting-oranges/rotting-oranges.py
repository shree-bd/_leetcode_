# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:

#         ROWS, COLS = len(grid), len(grid[0])
#         queue = deque()
#         fresh_count = 0

#         # Step 1: Add all rotten oranes to the queue ans count fresh orannges
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == 2:
#                     queue.append((r,c, 0))    # (row, col, time)
#                 elif grid[r][c] == 1:
#                     fresh_count += 1

                
#         # Step 2: BFS to rot adjacent fresh ornages
#         directions = [[1,0],[-1,0],[0,1],[0,-1]]
#         time = 0

#         while queue:
#             r, c, time = queue.popleft()

#             for dr, dc in directions:
#                 nr, nc = dr+r, dc+c

#                 # If adjacent cell is a frsh orange, rot it
#                 if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
#                     grid[nr][nc] = 2
#                     fresh_count -= 1
#                     queue.append((nr, nc, time + 1))


#         # Step 3: If any fresh oranges reamin, return -1
#         return time if fresh_count == 0 else -1
        

# from typing import List
# from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque([(r, c, 0) for r in range(rows) for c in range(cols) if grid[r][c] == 2])
        fresh = sum(cell == 1 for row in grid for cell in row)  # Count fresh oranges
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Directions (right, left, down, up)
        
        time = 0
        while queue:
            r, c, time = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Mark as rotten
                    fresh -= 1  # Reduce fresh orange count
                    queue.append((nr, nc, time + 1))  # Push to queue

        return time if fresh == 0 else -1  # If fresh oranges remain, return -1