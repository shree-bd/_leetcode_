class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        curr_sign = "+"
        num = 0
        last_num = 0
        result = 0

        for i, c  in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)

            if c in "+-/*" or i == len(s) - 1:
                if curr_sign == "+":
                    result += last_num
                    last_num = num
                elif curr_sign == "-":
                    result += last_num
                    last_num = -num
                elif curr_sign == "*":
                    last_num = last_num * num
                elif curr_sign == "/":
                    if last_num < 0:
                        last_num = -(-last_num//num)
                    else:
                        last_num = last_num // num
                curr_sign = c
                num = 0

        result += last_num
        return result


        """
        s = s.replace(' ', '')  # remove spaces
        result = 0
        last_num = 0
        num = 0
        sign = '+'
        
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)

            if c in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    result += last_num
                    last_num = num
                elif sign == '-':
                    result += last_num
                    last_num = -num
                elif sign == '*':
                    last_num = last_num * num
                elif sign == '/':
                    if last_num < 0:
                        last_num = -(-last_num // num)
                    else:
                        last_num = last_num // num

                sign = c
                num = 0

        result += last_num
        return result
        """


        