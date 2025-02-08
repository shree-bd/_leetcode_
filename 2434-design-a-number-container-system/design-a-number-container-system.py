class NumberContainers:
    def __init__(self):
        # Dictionary to map index to the number
        self.indexToNum = {}
        
        # Dictionary to map number to a SortedList of indices
        self.numToIndices = {}

    def change(self, index: int, number: int) -> None:
        # If index already exists, remove the old number from the list of indices
        if index in self.indexToNum:
            old_number = self.indexToNum[index]
            self.numToIndices[old_number].remove(index)
        
        # Update the index-to-number mapping
        self.indexToNum[index] = number
        
        # Add the index to the SortedList of the new number
        if number not in self.numToIndices:
            self.numToIndices[number] = SortedList()
        self.numToIndices[number].add(index)

    def find(self, number: int) -> int:
        # Return the smallest index for the given number (if it exists)
        if number in self.numToIndices and self.numToIndices[number]:
            return self.numToIndices[number][0]  # Return the smallest valid index
        return -1  # If no valid index found
        
# Time Complexity: O(log N)
# Space Complexity: O(N)



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)