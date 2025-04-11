class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        res = []

        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels:
                word += "ma"
            else:
                word = word[1:] + word[0] + "ma"
            word += "a" * (i+1)
            res.append(word)

        return " ".join(res)

            
# Time Complexity: O(N)
# Space Complexity: O(N)