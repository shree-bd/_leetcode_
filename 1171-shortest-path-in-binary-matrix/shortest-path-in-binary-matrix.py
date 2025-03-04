class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = collections.deque([(0,0,1)]) # row,column, distance
        visited = {(0,0)}
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        while queue:
            r, c, dist = queue.popleft()
            if r == N-1 and c == N-1:
                return dist

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    queue.append((nr,nc,dist+1))
                    visited.add((nr,nc))
        return -1 # no path found


# Time Complexity:  O(N^2)  (In the worst case, we traverse all N×N cells)
# Space Complexity:  O(N^2)  (In the worst case, all cells are stored in the queue).