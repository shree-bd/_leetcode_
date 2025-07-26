class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0
        n = len(s)

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]  # s[l] != s[r] now, so return previous window

        for i in range(n):
            p1 = expand(i,i)
            p2 = expand(i, i+1)
            # update longest
            res = max(p1,p2,res, key =len)
            
        return res





 