class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        two pass
        two stack: one to store open bracces
        secind to remove the closed ones
        """
        res =[]
        cnt = 0

        for c in s:
            if c == "(":
                res.append(c)
                cnt += 1
            elif c == ")" and cnt > 0:
                res.append(c)
                cnt -= 1
            elif c!= ")":
                res.append(c)

        filtered = []
        for c in res[::-1]:
            if c == "(" and cnt > 0:
                cnt -= 1
            else:
                filtered.append(c)
        return "".join(filtered[::-1])

        