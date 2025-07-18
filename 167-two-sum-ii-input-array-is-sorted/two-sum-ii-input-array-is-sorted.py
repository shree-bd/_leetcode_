class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        l, r = 0, len(numbers)-1

        while l <= r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1,r+1]
            elif total < target:
                l = l+1
            else:
                r = r - 1