class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat = [num for row in matrix for num in row]
        flat.sort()
        return flat[k-1]

        
        