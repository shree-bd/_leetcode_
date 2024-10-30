# class TimeMap:

#     def __init__(self):
#         self.store = {}
        

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.store:
#             self.store[key] = []
#         self.store[key].append([value, timestamp])
     
#     def get(self, key: str, timestamp: int) -> str:
#         res = ""
#         values = self.store.get(key, [])

#         # binary search
#         l, r = 0, len(values) - 1
#         while l <= r:
#             m = (l+r)//2
#             if values[m][1] <= timestamp:
#                 res = values[m][0]
#                 l = m+1
#             else:
#                 r = m-1
#         return res

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

from collections import defaultdict, deque
class TimeMap:

    def __init__(self):
        self.map = defaultdict(deque)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if self.map[key] and timestamp >= self.map[key][-1][0]:
            print(self.map[key][-1][1])
            return self.map[key][-1][1]
        val = ""
        l, r = 0, len(self.map[key]) - 1
        while l <= r:
            m = (l + r) // 2
            if self.map[key][m][0] == timestamp:
                return self.map[key][m][1]
            if self.map[key][m][0] > timestamp:
                r = m - 1
            else:
                val = self.map[key][m][1]
                l = m + 1
        return val


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)