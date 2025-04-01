# class Node:
#     def __init__(self, key, val):
#         self.key, self.val = key, val
#         self.prev = self.next = None

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = {}  # Map key to node

#         # Dummy nodes for LRU (left) and MRU (right)
#         self.left, self.right = Node(0, 0), Node(0, 0)
#         self.left.next, self.right.prev = self.right, self.left

#     # Remove a node from the doubly linked list
#     def remove(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next, nxt.prev = nxt, prev

#     # Insert a node at the right (most recently used position)
#     def insert(self, node):
#         prev, nxt = self.right.prev, self.right
#         prev.next = nxt.prev = node
#         node.next, node.prev = nxt, prev

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             # Move the accessed node to the most recently used position
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].val
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             # Remove the old node if the key already exists
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key])

#         if len(self.cache) > self.cap:
#             # Remove the least recently used node
#             lru = self.left.next
#             self.remove(lru)
#             del self.cache[lru.key]  # Fix: Remove from hashmap

        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# >>>>>>>>>>>>>> More concise soltuin using OrderedDict() <<<<<<<<<<<<<<<<<<

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity


    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.cap:
            self.cache.popitem(last=False)

        self.cache[key] = value
