class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in s:
            if stack and i.isdigit():
                stack.pop(-1)
            else:
                stack.append(i)
        return "".join(stack)


# Time Complexity: O(N)
# Space Complexity: O(N)