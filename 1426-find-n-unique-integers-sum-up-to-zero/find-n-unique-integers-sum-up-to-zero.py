class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        
        # Add pairs (x, -x) to ensure sum is zero
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)

        # If n is odd, add 0 to maintain sum as zero
        if n % 2 == 1:
            result.append(0)

        return result


# Time Complexity: O(N)
# Space Complexity: O(N)
