class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):  # Iterating using index
            if s[i] != "]":
                stack.append(s[i])  # Appending as list (unnecessary nesting)
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr  # O(N²) due to repeated concatenation
                stack.pop()  # Remove "["

                k = ""

                while stack and stack[-1].isdigit():
                    k = stack.pop() + k  # Building multiplier string
                stack.append(int(k) * substr)  # Repeating and appending the result

        return "".join(stack)  # Joining at the end

# Time Complexity: O()
# Space Complesity: O()
        