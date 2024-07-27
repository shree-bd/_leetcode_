class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        # Initialize indices for both words
        i,j=0,0

        # merge the words alternatively
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i+=1
            j+=1
        merged.append(word1[i:])
        merged.append(word2[j:])
        # # Append remaining letters fro word1 if any
        # while i < len(word1):
        #     merged.append(word1[i])
        #     i+=1

        # # Append remaining letters fro word1 if any
        # while j < len(word2):
        #     merged.append(word2[j])
        #     j+=1
        return "".join(merged)

        