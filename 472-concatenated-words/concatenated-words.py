class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        res = []

        @lru_cache(None)  # Memoization
        def dfs(word):
            for i in range(1, len(word)):  # Try splitting at every position
                prefix = word[:i]
                suffix = word[i:]

                if (prefix in wordSet and suffix in wordSet) or (prefix in wordSet and dfs(suffix)):
                    return True
            return False  # Base case: If no valid split is found

        for word in words:
            wordSet.remove(word)  # Remove current word to avoid self-usage
            if dfs(word):
                res.append(word)
            wordSet.add(word)  # Add back after checking

        return res

        
# Time Complexity: O(N * L^2) (with memoization)
# Space Complexity: O(N * L)