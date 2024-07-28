class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]  # List of lists to handle collisions

    def _hash(self,key):
        return key % self.size
        
    def put(self, key: int, value: int) -> None:
        # calculate index using hash function
        index = self._hash(key)
        # check if the key already existes in the map
        for i, (k,v) in enumerate(self.map[index]):
            if k == key:
                self.map[index][i] = (key, value)  #updtae value if key exists
                return
        # otherwise, append the new k-v pair
        self.map[index].append((key,value))
        

    def get(self, key: int) -> int:
        # calculate index using hash function
        index = self._hash(key)
        # search for the key in th elist at computed index
        for k,v in self.map[index]:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        # calculate index using hash function
        index = self._hash(key)
        # search for the key in the list at computed index
        for i, (k,v) in enumerate(self.map[index]):
            if  k == key:
                # removethe key-value pair if key is found
                del self.map[index][i]
                return

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)