class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        arr.sort()
        n = len(arr)
        for i in range(n - 2):
            curr = arr[i]
            l, r = i+1, n - 1
            while l < r:
                if curr + arr[l] + arr[r] < target:
                    l += 1
                elif curr + arr[l] + arr[r] > target:
                    r -= 1
                else:
                    if arr[l] == arr[r]:
                        ans += ((r - l + 1) * (r - l))// 2
                        break
                    else:
                        countl = countr = 0
                        curr_l, curr_r = arr[l], arr[r]
                        while arr[l] == curr_l:
                            countl += 1
                            l += 1
                        while arr[r] == curr_r:
                            countr += 1
                            r -= 1
                        ans += (countr * countl)
        return ans % ((10**9) + 7)


