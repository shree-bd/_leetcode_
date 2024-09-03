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

        

        # alist=list(string.ascii_lowercase)
        #         val="".join(str(alist.index(i)+1) for i in s)
        #         for _ in range(k):
        #             val=str(sum(int(digit) for digit in val))

        #         return int(val)