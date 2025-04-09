class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        left_rem, right_rem = self.get_misplaced(s)

        def dfs(i, path, open_count, l_rem, r_rem):
            if i == len(s):
                if open_count == 0 and l_rem == 0 and r_rem == 0:
                    res.add(path)
                return

            c = s[i]

            if c == '(':
                # Option 1: remove
                if l_rem > 0:
                    dfs(i+1, path, open_count, l_rem - 1, r_rem)
                # Option 2: keep
                dfs(i+1, path + '(', open_count + 1, l_rem, r_rem)

            elif c == ')':
                # Option 1: remove
                if r_rem > 0:
                    dfs(i+1, path, open_count, l_rem, r_rem - 1)
                # Option 2: keep (only if there’s a matching '(')
                if open_count > 0:
                    dfs(i+1, path + ')', open_count - 1, l_rem, r_rem)

            else:
                # Always keep non-parens
                dfs(i+1, path + c, open_count, l_rem, r_rem)

        dfs(0, "", 0, left_rem, right_rem)
        return list(res)

    def get_misplaced(self, s):
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left, right
        