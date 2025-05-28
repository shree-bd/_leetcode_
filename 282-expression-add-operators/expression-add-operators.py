class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def backtrack(idx, path, value, prev):
            if idx == len(num):
                if value == target:
                    res.append(path)
                return

            for i in range(idx, len(num)):
                if i>idx and num[idx] == '0':
                    break

                curr_str = num[idx:i+1]
                curr_num = int(curr_str)

                if idx == 0:
                    backtrack(i+1, curr_str, curr_num, curr_num)
                else:
                    backtrack(i+1, path + "+" + curr_str, value + curr_num, curr_num)
                    backtrack(i+1, path + "-" + curr_str, value - curr_num, -curr_num)
                    backtrack(i+1, path + "*" + curr_str, value - prev + (prev * curr_num), prev * curr_num)

        backtrack(0, "", 0, 0)
        return res
        