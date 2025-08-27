class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # i -> pointer in s, j -> pointer in t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # move s pointer only on match
            j += 1  # always move t pointer

        # if we matched all of s, return True
        return i == len(s)
    
# T.C: O() | S.C: O()