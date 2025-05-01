class Solution:
    def simplifyPath(self, path: str) -> str:

        parts = path.split("/")

        stack = []

        for c in parts:
            if c == "." or c == "":
                continue
            elif c == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return "/" + "/".join(stack)


        