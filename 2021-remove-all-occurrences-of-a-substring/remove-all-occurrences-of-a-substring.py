class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # stack, sub_len = [], len(part)
        # for char in s:
        #     stack.append(char)
        #     if "".join(stack[-sub_len:]) == part:
        #         del stack[-sub_len:]
        # return "".join(stack)


        i, n = 0, len(s)
        s = list(s)  # Convert to list for efficient modifications
        part_len = len(part)

        for j in range(n):
            s[i] = s[j]
            i += 1

            if i >= part_len and "".join(s[i - part_len:i]) == part:
                i -= part_len  # Remove `part` by rolling back `i`

        return "".join(s[:i])