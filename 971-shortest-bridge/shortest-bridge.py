class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def invalid(r, c):
            return r < 0 or c < 0 or r >= N or c >= N
        
        visit = set()
        def dfs(r, c):
            if invalid(r, c) or not grid[r][c] or (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        def bfs():
            res, q = 0, deque(visit)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        curR, curC = r + dr, c + dc
                        if invalid(curR, curC) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC] == 1:
                            return res
                        q.append((curR, curC))
                        visit.add((curR, curC))
                res += 1

        # 1. Find the first island and mark it with DFS
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()

# T.C: O(N^2) | S.C: O(N^2)
        