class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)

        # Add the integers
        sum_num = num1 + num2

        # Convert the result back to a binary string and remove '0b' prefix
        binary_sum = bin(sum_num)[2:]

        return binary_sum
            