class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # final_sum = int(num1)+ int(num2)
        # return str(final_sum)
        i, j = len(num1)-1, len(num2)-1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            cur_i = int(num1[i]) if i >= 0 else 0
            cur_j = int(num2[j]) if j >= 0 else 0

            cur_sum = carry + cur_i + cur_j

            res.append(str(cur_sum % 10))

            carry = cur_sum // 10

            i, j = i - 1, j - 1

        # if carry:
        #     res.append(str(carry))

        return "".join(reversed(res))

# Time Complexity: O(max(len(num1), len(num2))
# Space Complexity: O(N)

        