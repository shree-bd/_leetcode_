class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        return s == s[::-1]

        # left, right = 0, len(s)-1

        # while left < right:
        #     if s[left] != s[right]:
        #         return False

        #     left += 1
        #     right -= 1

        # return True


