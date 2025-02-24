class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])
        res = []
        r, c, direction = 0, 0, 1

        for _ in range(rows*cols):
            res.append(mat[r][c])

            if direction ==1:
                if c == cols-1:
                    r += 1
                    direction = -1
                elif r == 0:                    
                    c += 1
                    direction = -1
                else:
                    r -= 1
                    c += 1
            else:
                if r == rows - 1:
                    c += 1
                    direction = 1
                elif c== 0:
                    r += 1
                    direction = 1
                else:
                    r += 1
                    c -= 1
                
        return res

        