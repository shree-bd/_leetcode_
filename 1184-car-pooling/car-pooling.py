class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        change = [0] * 1001

        for passenger, start, end in trips:
            for i in range(start, end):
                change[i] += passenger
                if change[i] > capacity:
                    return False

        return True
        