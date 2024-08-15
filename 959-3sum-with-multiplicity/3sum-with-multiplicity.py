class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ret = 0
        arr.sort()
        for i in range(len(arr) - 2):
            curr = arr[i]
            r = len(arr) - 1
            l = i + 1
            while l < r:
                if curr + arr[l] + arr[r] < target:
                    l += 1
                elif curr + arr[l] + arr[r] > target:
                    r -= 1
                else:
                    if arr[l] == arr[r]:
                        ret += ((r - l + 1) * (r - l))// 2
                        break
                    else:
                        countl = 0
                        countr = 0
                        curr_l, curr_r = arr[l], arr[r]
                        while arr[l] == curr_l:
                            countl += 1
                            l += 1
                        while arr[r] == curr_r:
                            countr += 1
                            r -= 1
                        ret += (countr * countl)
        return ret % ((10**9) + 7)


