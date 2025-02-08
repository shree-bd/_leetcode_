class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []

        words = s.split()

        for word in words:
            stack.append(word)


        return " ".join(stack[::-1])
        