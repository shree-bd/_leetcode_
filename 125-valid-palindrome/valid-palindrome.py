class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alpha(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))

        left, right = 0, len(s)-1

        while left < right:
            while left < right and not is_alpha(s[left]):
                left += 1
            while left < right and not is_alpha(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left+1,right-1
        return True
        