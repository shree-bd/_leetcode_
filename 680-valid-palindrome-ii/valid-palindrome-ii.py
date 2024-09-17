class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome_range(i, j):
            """Helper function to check if s[i:j+1] is a palindrome."""
            return all(s[k] == s[j - k + i] for k in range(i, j))
        
        # Two pointers approach
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                # If s[i] != s[j], try skipping one character either from the left or right
                return is_palindrome_range(i + 1, j) or is_palindrome_range(i, j - 1)
            i += 1
            j -= 1
        
        return True  # If no mismatches, it's a palindrome