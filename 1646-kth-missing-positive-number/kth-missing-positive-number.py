class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        missing = []
        num = 1

        while len(missing) < k:
            if num not in arr_set:
                missing.append(num)
            num += 1
        return missing[-1]





        # left, right = 0, len(arr)

        # while left < right:
        #     mid = (left+right)//2
        #     missing = arr[mid] - (mid+1)
        #     if missing < k:
        #         left = mid + 1
        #     else:
        #         right = mid

        # return left + k

# Time Complexity: O(N log N)
# Space  Complexity: O()



        