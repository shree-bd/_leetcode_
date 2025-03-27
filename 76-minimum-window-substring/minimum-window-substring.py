class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_map = Counter(t)
        have_map = {}

        have, need = 0, len(t_map)
        min_len = float("inf")
        left = 0
        res = [-1, -1]

        for right, char in enumerate(s):
            have_map[char] = have_map.get(char, 0) + 1

            if char in t_map and have_map[char] == t_map[char]:
                have += 1

            while have == need:
                if (right - left + 1) < min_len:
                    res = [left, right]
                    min_len = right - left + 1

                # Shrink the window from the left
                have_map[s[left]] -= 1
                if s[left] in t_map and have_map[s[left]] < t_map[s[left]]:
                    have -= 1
                left += 1  # Move left pointer

        # Extract final substring
        if min_len == float("inf"):
            return ""
        left, right = res
        return s[left:right+1]

# Time Complexity: O(N)
# Space Complexity: O(N) (due to `Counter` dictionary)


        