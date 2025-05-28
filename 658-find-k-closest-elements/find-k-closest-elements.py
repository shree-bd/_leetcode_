# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>binary search approach<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-k

        while l < r:
            mid = (l+r)//2
            if x - arr[mid] > arr[mid+k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[l:l+k]
            
# Time Complexity: O(log(N-k) + k)
# Space Complexity: O(1)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>min heap approach<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         min_heap = []

#         for num in arr:
#             heapq.heappush(min_heap, (abs(num-x), num)) # stores (diff,element)

#         res = []
#         while k > 0:
#             res.append(heapq.heappop(min_heap)[1])
#             k -= 1        

#         return sorted(res)

# Time Complexity: O(K log N)
# Space Complexity: O(N)
        
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>sorting approach<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         arr.sort(key = lambda num: abs(num-x))
#         return sorted(arr[:k])

# Time Complexity: O(N log N)
# Space Complexity: O(K)
        