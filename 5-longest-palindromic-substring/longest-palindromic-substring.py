class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0
        n = len(s)

        def expand_center(left,right):
            nonlocal res, res_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_len = right - left + 1
                if curr_len > res_len:
                    res = s[left:right+1]
                    res_len = curr_len
                left -= 1
                right += 1

        for i in range(n):
            expand_center(i,i)
            expand_center(i,i+1)
        
        return res



            
        