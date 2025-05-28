class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        change = [0] * 1001

        for passengers, start, end in trips:
            change[start] += passengers
            change[end] -= passengers

        curr = 0
        for c in change:
            curr += c
            if curr > capacity: return False
        return True

# Time Complexity: O(N) | Space Complexity: O(R) R -> diff array of size 1001

"""
# BRUTE FORCE
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        change = [0] * 1001

        for passenger, start, end in trips:
            for i in range(start, end):
                change[i] += passenger
                if change[i] > capacity:
                    return False

        return True
        
# Time Complexity: O(T*R) | Space Complexity: O(1)

"""