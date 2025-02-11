class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # stack, sub_len = [], len(part)
        # for char in s:
        #     stack.append(char)
        #     if "".join(stack[-sub_len:]) == part:
        #         del stack[-sub_len:]
        # return "".join(stack)


        while 1:
            if part in s:
                s=s.replace(part, "", 1)
            else:
                break
        return s