class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        # this ignores multiple s[aces automatically]
        words = s.split()
        #push words onto stack
        for word in words:
            stack.append(word)
        #pop words in reversed order
        return " ".join(stack[::-1])


# Time Complexity: O(N)
# Space Complexity: O(N)