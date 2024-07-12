class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index == -1:
            return word

        rev_str = word[:index+1][::-1]

        result = rev_str + word[index + 1:]

        return result
        


        