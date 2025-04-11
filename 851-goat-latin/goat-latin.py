class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        res = []

        for i, word in enumerate(words, 1):
            if word[0] not in vowels:
                word = word[1:] + word[0] + "ma"
            else:
                word += "ma"
            
            word += "a" * i
            res.append(word)

        return " ".join(res)




            
# Time Complexity: O(N)
# Space Complexity: O(N)