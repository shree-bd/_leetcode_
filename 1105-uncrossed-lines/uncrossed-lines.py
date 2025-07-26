class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m,n = len(nums1), len(nums2)

        dp = [[0] * (n+1) for _ in range(m+1)]
        # dp = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1]) 

        return dp[0][0]


        """
        # memoization -> dp
        def dfs(i, j ):
            if i == len(nums1) or j == len(nums2):
                return 0

            if (i,j) in dp:
                return dp[(i,j)]

            if nums1[i] == nums2[j]:
                dp[(i,j)] = 1 + dfs(i+1, j+1)
            else:
                dp[(i,j)] = max(dfs(i+1,j), dfs(i, j+1))
            return dp[(i,j)]

        dp = {}
        return dfs(0,0)
        """
        