class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = n
        if N < 0:
            x  = 1/x
            N = -N

        result = 1.0
        curr_product = x

        while N>0:
            if N%2==1:
                result *= curr_product
            curr_product *= curr_product
            N //= 2

        return result

        
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