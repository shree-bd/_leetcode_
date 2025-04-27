class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        res = 0

        for k,cnt in count.items():
            group_size = k + 1
            groups = math.ceil(cnt/group_size)
            res += groups * group_size

        return res

# T.C: O(N) | S.C: O(N)
        