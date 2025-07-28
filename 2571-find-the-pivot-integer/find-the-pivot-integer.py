class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n+1)//2
        sqrt = int(total ** 0.5)

        if sqrt * sqrt == total:
            return sqrt
        return -1
        