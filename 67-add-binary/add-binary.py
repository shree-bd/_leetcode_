
            
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        carry = 0

        a,b = a[::-1],b[::-1]
        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total%2)
            ans = char + ans
            carry = total //2

        if carry:
            ans = "1" +ans
        return ans







# by using python function

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         num1 = int(a, 2)
#         num2 = int(b, 2)

#         # Add the integers
#         sum_num = num1 + num2

#         # Convert the result back to a binary string and remove '0b' prefix
#         binary_sum = bin(sum_num)[2:]

#         return binary_sum