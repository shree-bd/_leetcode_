class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        char1 = s1.split()
        char2 = s2.split()

        word_count = Counter(char1) + Counter(char2)

        return [word for word, count in word_count.items() if count == 1]
