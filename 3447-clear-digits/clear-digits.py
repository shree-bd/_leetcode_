class Solution:
    def clearDigits(self, s: str) -> str:
        res = []

        def isdigit(c):
            return ord("0") <= ord(c) <= ord("9")

        for c in s:
            if isdigit(c):
                if res:  # Ensure we don't pop from an empty list
                    res.pop()
            else:
                res.append(c)

        return "".join(res)


# Time Complexity: O(N)
# Space Complexity: O(N)