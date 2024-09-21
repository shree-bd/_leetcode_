class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g_sort = g.sort()
        s_sort = s.sort()
        satisfied = 0
        i,j =0,0
    
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:  # If cookie size >= child's greed
                satisfied += 1
                i += 1
            j += 1
                    
                
        return satisfied



        