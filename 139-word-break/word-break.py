# Top down apparoach:
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n+1) # create a DP aaray 
        dp[0] = True #Base case: empty string can always be segmented

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break # Found a valid segmentation
        return dp[n] # Return whether the entire string can be segmented


#Bottom up appraoch
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         word_set = set(wordDict)
#         n = len(s)
#         dp = [False] * (n+1) # create a DP aaray 
#         dp[n] = True #Base case: empty string can always be segmented

#         for i in range(n-1, -1, -1):
#             for w in wordDict:
#                 if (i+len(w)) <= n and s[i: i+len(w)] == w:
#                     dp[i] = dp[i+len(w)]
#                 if dp[i]:
#                     break

#         return dp[0]





        