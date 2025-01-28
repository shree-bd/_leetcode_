class RandomizedSet:

    def __init__(self):
        self.numMap = {}  # Dictionary to store value-to-index mapping
        self.numList = []  # List to store values
        
    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        self.numMap[val] = len(self.numList)  # Map the value to the current list length
        self.numList.append(val)  # Add the value to the list
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        # Swap the element to remove with the last element
        last_val = self.numList[-1]
        idx_to_remove = self.numMap[val]
        self.numList[idx_to_remove] = last_val  # Replace the value with the last one
        self.numMap[last_val] = idx_to_remove  # Update the index of the last value
        # Remove the last element
        self.numList.pop()
        del self.numMap[val]  # Remove the value from the dictionary
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()