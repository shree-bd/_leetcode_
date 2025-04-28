class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix.append(prefix_sum)
        

    def pickIndex(self) -> int:
        total = self.prefix[-1]
        target = random.randint(1, total)

        # Manual binary search
        low, high = 0, len(self.prefix) - 1
        while low < high:
            mid = (low + high) // 2
            if self.prefix[mid] < target:
                low = mid + 1
            else:
                high = mid

        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()