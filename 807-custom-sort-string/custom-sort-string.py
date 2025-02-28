class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = collections.Counter(s)
        res = []

        for char in order:
            if char in count:
                res.append(char * count[char])
                del count[char]

        for char, freq in count.items():
            res.append(char * freq)

        return "".join(res)

# Time Complexity: O(N+M)
# Space Complexiyt: O(N) counter(s) takes O(N)
                
        
        