class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res 
        

# Time Complexity: O(n), since both left and right traverse the string once.
# Space Complexity: O(k), where k is the size of the character set (e.g., 26 for lowercase English letters).