class Solution:
    def reverseWords(self, s: str) -> str:
        result = ' '.join(word[::-1] for word in s.split())
        return result
