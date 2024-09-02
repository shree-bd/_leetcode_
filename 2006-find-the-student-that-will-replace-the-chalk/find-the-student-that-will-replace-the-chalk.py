class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)

        k = k%total

        for i,chalk_needed in enumerate(chalk):
            if chalk_needed > k:
                return i
            k = k-chalk_needed

        # return -1
