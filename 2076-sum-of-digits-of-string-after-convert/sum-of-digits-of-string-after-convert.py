class Solution:
    def getLucky(self, s: str, k: int) -> int:
        pattern = {chr(i): i - 96 for i in range(97, 123)}
        res = ""

        for ch in s:
            value = str(pattern.get(ch.lower(),""))
            res += value
            
        for _ in range(k):
            digit_sum = sum(int(digit) for digit in res)
            res = str(digit_sum)

        return int(res)

        