class Solution:

    def __init__(self, nums: List[int]):
        self.hash_map = {}
        for i, num in enumerate(nums):
            if num not in self.hash_map:
                self.hash_map[num] = []
            self.hash_map[num].append(i)
        

    def pick(self, target: int) -> int:
        return random.choice(self.hash_map[target])

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)