class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # return len(set(nums) - {0})

        cnt = int(0)

        nums = [x for x in nums if x!= 0]

        while nums:
            minNum = min(nums)

            nums = [x - minNum for x in nums if (x - minNum) != 0]
            cnt += 1

        return cnt

        