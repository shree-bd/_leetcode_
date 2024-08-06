class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_dict = {}
        for i in arr:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        
        count = 0
        for i in arr:
            if count_dict[i] == 1:
                count += 1
                if count == k:
                    return i

        return ''
                 
        