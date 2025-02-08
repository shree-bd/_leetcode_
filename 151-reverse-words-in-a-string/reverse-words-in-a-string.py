class Solution:
    def reverseWords(self, s: str) -> str:
        # Convert string to list to allow in-place modifications
        s = list(s.strip())  # Trim leading/trailing spaces
        
        # Step 1: Reverse the entire string
        self.reverse(s, 0, len(s) - 1)

        # Step 2: Reverse each word
        n = len(s)
        start = 0
        
        while start < n:
            if s[start] != " ":
                end = start
                while end < n and s[end] != " ":
                    end += 1
                self.reverse(s, start, end - 1)
                start = end
            start += 1  # Skip spaces
        
        # Step 3: Remove extra spaces (handle in-place)
        return self.clean_spaces(s)

    def reverse(self, s, left, right):
        """Helper function to reverse a portion of the list"""
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def clean_spaces(self, s):
        """Helper function to remove extra spaces in-place"""
        i = 0
        for j in range(len(s)):
            if s[j] != " " or (i > 0 and s[i - 1] != " "):
                s[i] = s[j]
                i += 1
        return "".join(s[:i])  # Convert list back to string