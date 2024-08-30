class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []

        low = 0
        high = len(s)

        for i in range(len(s)):
            if s[i] == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1

        res.append(low)
        return res
        