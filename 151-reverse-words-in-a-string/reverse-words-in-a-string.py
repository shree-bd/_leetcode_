class Solution:
    def reverseWords(self, s: str) -> str:
        # stack = []
        # # this ignores multiple s[aces automatically]
        # words = s.split()
        # #push words onto stack
        # for word in words:
        #     stack.append(word)
        # #pop words in reversed order
        # return " ".join(stack[::-1])


        words = s.split()
        left, right = 0, len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words) 

# Time Complexity: O(N)
# Space Complexity: O(N)