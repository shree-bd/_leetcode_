class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        countMap = {}
        for i in arr:
            if i in countMap:
                countMap[i] += 1
            else:
                countMap[i] = 1
        
        count = 0
        for i in arr:
            if countMap[i] == 1:
                count += 1
                if count == k:
                    return i

        return ''
                 
        