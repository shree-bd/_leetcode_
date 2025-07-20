class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # if len(s) != len(t):
        #     return False

        # count_s, count_t = {} , {}
        # count_s = s.Counter()
        # count_t = t.Counter()