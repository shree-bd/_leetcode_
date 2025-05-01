class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        
        def helper(x,n):
            if n == 0: return 1
            res = helper(x*x,n//2)
            return x * res if n%2==1 else res

        res = helper(x,abs(n))
        return res if n>0 else 1/res




        