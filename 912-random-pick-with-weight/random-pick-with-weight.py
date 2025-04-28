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
        idx = bisect.bisect_left(self.prefix, target)
        return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()