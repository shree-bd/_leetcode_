class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindrome(s, l, r):
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l,r = l-1, r+1
            return cnt
        res = 0
        for i in range(len(s)):            
            res += countPalindrome(s, i, i)
            res += countPalindrome(s, i, i+1)
        return res

# Time Complexity: O(N^2) | Space Complexity: O(N)

"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l, r = l-1, r+1

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l, r = l-1, r+1

        return res

# Time Complexity: O(N^2) | Space Complexity: O(N)

"""

