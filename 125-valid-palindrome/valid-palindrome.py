# using manual aphanumeric func: time comeplxity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))




#  Using built in function
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())

        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# Time Complexity: O(N)
# Space Complexity: O(N)
"""