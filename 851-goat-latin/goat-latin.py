class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        res = []

        for i, word in enumerate(words, 1):
            if word[0] not in vowels:
                goat = word[1:] + word[0] + "ma"
            else:
                goat = word + "ma"

            res.append(goat + "a" * i)

        return " ".join(res)

            
# Time Complexity: O(N)
# Space Complexity: O(N)