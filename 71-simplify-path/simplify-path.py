class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        parts = path.split("/")

        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)

        #  /home/a/b


             
# Time Complexity: O(N)
# Space Complexity: O(N)

"""
Input: "/a/./b/../../c/"
Steps:
- 'a' → push to stack
- '.' → ignore
- 'b' → push to stack
- '..' → pop 'b'
- '..' → pop 'a'
- 'c' → push to stack

Output: "/c"
"""