class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_to_bit = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}  # Mapping vowels to bits
        current_mask = 0  # Initialize bitmask to 0 (all vowels even)
        max_len = 0  # Variable to store the maximum length of the substring
        mask_index_map = {0: -1}  # To store the first occurrence of each bitmask
        
        for i, char in enumerate(s):
            # If the character is a vowel, toggle its corresponding bit in the mask
            if char in vowel_to_bit:
                current_mask ^= vowel_to_bit[char]
            
            # If we have seen the current mask before, calculate the length of the substring
            if current_mask in mask_index_map:
                max_len = max(max_len, i - mask_index_map[current_mask])
            else:
                # Otherwise, store the first occurrence of the current mask
                mask_index_map[current_mask] = i
        
        return max_len
        