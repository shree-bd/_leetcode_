class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        current_sum = 0

        for weight in w:
            current_sum += weight
            self.prefix_sums.append(current_sum)
        self.total_sum = current_sum                 # Total sum. of weights
        

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)

        # Perform binary search
        l, r = 0, len(self.prefix_sums) - 1
        while l < r:
            mid = (l+r)//2
            if self.prefix_sums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()