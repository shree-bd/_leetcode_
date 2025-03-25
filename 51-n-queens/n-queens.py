class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diagonal = set()
        neg_diagonal = set()
        res = []
        board = [["."]*n for _ in range(n)]

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r+c) in pos_diagonal or (r-c) in neg_diagonal:
                    continue

                cols.add(c)
                pos_diagonal.add(r+c)
                neg_diagonal.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                pos_diagonal.remove(r+c)
                neg_diagonal.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res




# Time Ciomplexity: O(N!)
# Space Complexity: O(N^2)