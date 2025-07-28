class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n+1)//2

        for x in range(1, n+1):
            left = x*(x+1)//2
            right = total - (x-1)*x //2
            if left == right:
                return x
        return -1

        """
        sqrt = int(total ** 0.5)

        if sqrt * sqrt == total:
            return sqrt
        return -1
        """
        