class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        neg = n <0
        n = abs(n)

        result = 1.0
        while n:
            if n%2==1:
                result *= x
            x *= x
            n//=2
        return 1/result if neg else result

        
# Time Complexity: O(log N)
# Space Complexity: O(1)













        # if x == 0: return 0

        # def helper(x,n):            
        #     if n == 0: return 1

        #     # Recursive case: Compute the result for the smaller problem (x^(n//2))
        #     res = helper(x * x, n // 2)              # Use x^2 and halve n
        #     return x * res if n % 2 else res

        # res = helper(x, abs(n))
        # return res if n>= 0 else 1/res



# Time Complexity: O(log n)
# Space Complexity: O(log n)