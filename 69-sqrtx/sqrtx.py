class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            return None
        
        if x == 0 or x == 1:
            return x

        # Binary Search
        first, last = 1, x
        res = 0

        while first <= last:
            mid = first + ((last-first)//2)

            if (mid**2) > x:
                last = mid-1
            elif (mid**2) < x:
                first = mid+1
                res = mid
            else:
                return mid
        return res




        return last
        
