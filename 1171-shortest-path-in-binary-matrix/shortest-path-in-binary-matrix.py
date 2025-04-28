class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        visited = set((0,0))

        while queue:
            r, c, length = queue.popleft()

            if (r, c) == (n-1, n-1):
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr, nc, length+1))

        return -1