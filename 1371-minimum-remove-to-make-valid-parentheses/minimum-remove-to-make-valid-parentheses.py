class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        cnt = 0
        # First pass: Remove extra closing parentheses ')'
        for c in s:
            if c == "(":
                res.append(c)
                cnt += 1
            elif c == ")" and cnt > 0:
                res.append(c)
                cnt -= 1
            elif c!= ")":
                res.append(c)

        # Second pass: Remove extra opening parentheses '('
        filtered = []
        for c in res[::-1]:
            if c == "(" and cnt > 0:
                cnt -= 1  # Skip this extra '('
            else:
                filtered.append(c)

        return "".join(filtered[::-1])


# Time Complexity: O(N)
# Space Complxity: O(N)

         