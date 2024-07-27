class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s)-1
        while left <= right:
            if s[left]!=s[right]:
                # Make both characters the same to form the smallest palindrome
                min_char = min(s[left],s[right])
                s[left]=s[right]=min_char
            left+=1
            right-=1
        return ''.join(s)
        