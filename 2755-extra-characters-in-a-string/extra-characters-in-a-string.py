class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        word_set = set(dictionary)   # convert list to set for O(1) lookups
        dp = { len(s): 0 }

        def dfs(i):
            if  i == len(s):
                return 0

            if i in dp:
                return dp[i]

            res = 1 + dfs(i+1)
            for j in range(i, len(s)):
                if s[i:j+1] in word_set:
                    res = min(res, dfs(j+1))

            dp[i] = res
            return res

        return dfs(0)

            

         
       
       
# Time Complexity : O(n^2)
# Space Complexity : O(n+m)