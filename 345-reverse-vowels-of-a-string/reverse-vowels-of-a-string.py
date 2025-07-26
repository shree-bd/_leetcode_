class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        stack = []

        for ch in s:
            if ch in vowels:
                stack.append(ch)

        res = []
        for ch in s:
            if ch in vowels:
                res.append(stack.pop())
            else:
                res.append(ch)

        return "".join(res)
        