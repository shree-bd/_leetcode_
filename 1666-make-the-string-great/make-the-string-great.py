class Solution:
    def makeGood(self, s: str) -> str:
        s= list(s)
        i = 0

        for j in range(len(s)):
            s[i] = s[j]
            if i > 0 and abs(ord(s[i]) - ord(s[i-1])) == 32:
                i -= 1
            else:
                i += 1

        return "".join(s[:i])