class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        current_number = 0  # Tracks the number being formed from consecutive digits
        last_value = 0      # Last value used in multiplication or division
        result = 0          # Final accumulated result
        last_operator = "+" # Keeps track of the last operator seen

        while i < len(s):   # Loop through the string
            char = s[i]

            if char.isdigit():  # If the character is a digit
                current_number = current_number * 10 + int(char)  # Build the number
            
            if char in "+-*/" or i == len(s) - 1:  # If an operator or end of string
                if last_operator == "+":           # If the last operator is '+'
                    result += current_number       # Add the current number to the result
                    last_value = current_number    # Update last_value
                elif last_operator == "-":         # If the last operator is '-'
                    result -= current_number       # Subtract the current number
                    last_value = -current_number   # Update last_value
                elif last_operator == "*":         # If the last operator is '*'
                    result -= last_value           # Remove the effect of last_value
                    last_value = last_value * current_number  # Multiply last_value
                    result += last_value           # Add updated last_value
                elif last_operator == "/":         # If the last operator is '/'
                    result -= last_value           # Remove the effect of last_value
                    last_value = int(last_value / current_number)  # Perform truncating division
                    result += last_value           # Add updated last_value
                
                last_operator = char               # Update the last operator
                current_number = 0                 # Reset current_number
            
            i += 1                                 # Move to the next character

        return result                              # Return the final result
