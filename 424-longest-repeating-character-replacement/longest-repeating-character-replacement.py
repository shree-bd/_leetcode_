class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        charMap = {}

        for r in range(len(s)):
            charMap[s[r]] = 1 + charMap.get(s[r], 0)

            while (r - l + 1) - max(charMap.values()) > k:
                charMap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
                
        





# Time Complexity: O(n) Each character is processed once as the window expands or contracts.
# Space Complexity: O(1) The character count map uses at most 26 entries (for English uppercase letters).
