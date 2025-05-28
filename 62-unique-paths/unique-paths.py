class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for i in range(m-1):
            new_row = [1] * n
            for j in range(n-2, -1, -1):
                new_row[j] = new_row[j+1] + dp[j]
            dp = new_row

        return dp[0]

# Time Complexity: O(M*N)
# Space Complexity: O(N)