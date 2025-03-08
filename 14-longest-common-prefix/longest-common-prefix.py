class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()
        first, last = strs[0], strs[-1]
        i = 0

        while i < len(first) and i<len(last) and first[i] == last[i]:
            i += 1
        return first[:i]
















        # if not strs:
        #     return ""

        # prefix = strs[0]  # Start with the first word as the prefix

        # for word in strs[1:]:  # Compare with all other words
        #     while not word.startswith(prefix):  # Keep reducing prefix until match
        #         prefix = prefix[:-1]  # Remove last character
        #         if not prefix:
        #             return ""  # If prefix becomes empty, return ""

        # return prefix







            # OR

        # strs.sort()
        # first, last = strs[0], strs[-1]
        # i = 0

        # while i < len(first) and i < len(last) and first[i] == last[i]:
        #     i +=1
        # return first[:i]
        
        
# Time Complexity: O(N log N)
# Space Complexity: O(1)