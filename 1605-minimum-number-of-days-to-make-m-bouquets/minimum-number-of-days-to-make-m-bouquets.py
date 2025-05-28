class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isPossible(days):
            cnt = 0
            num_bouquets = 0
            for d in bloomDay:
                if d <= days:
                    cnt += 1
                    if cnt == k:
                        num_bouquets += 1
                        cnt = 0
                else:
                    cnt = 0
            return num_bouquets >= m


        if m * k > len(bloomDay):
            return -1 # not enoguh flowers total

        left, right = min(bloomDay), max(bloomDay)
        res = -1
        while left <= right:
            mid = (left+right)//2
            if isPossible(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

# Time Complexity: O(n * log D)
# Space Complexity: O(1)





        