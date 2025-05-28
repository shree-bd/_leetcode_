# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>reservoir sampling<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.indices = defaultdict(list)

    def pick(self, target: int) -> int:
        if target in self.indices:
            return self.indices[target][
                randint(0, len(self.indices[target])-1)
            ]

        count = 0
        result = None

        # Iterate over the nums array and apply reservoir sampling
        for i, num in enumerate(self.nums):
            if num == target:
                # Reservoir sampling: pick with probability 1/count
                if result is None or random.randint(0, count) == 0:
                    result = i
                count += 1

            self.indices[num].append(i)
        return result


# Time Complexity: O(N) per pick call
# Space Complexity: O(1)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>brute force(hash_map) approach<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# class Solution:

#     def __init__(self, nums: List[int]):
#         self.hash_map = {}
#         for i, num in enumerate(nums):
#             if num not in self.hash_map:
#                 self.hash_map[num] = []
#             self.hash_map[num].append(i)
        

#     def pick(self, target: int) -> int:
#         return random.choice(self.hash_map[target])

# Time Complexity: O(N)
# Space Complexity: O(N)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)