class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self._remove(node)
        self._add(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]

            self._remove(old_node)

        node = ListNode(key, value)
        self.cache[key] = node
        self._add(node)

        if len(self.cache) > self.capacity:
            node_to_delete = self.head.next
            self._remove(node_to_delete)

            del self.cache[node_to_delete.key]

    
    def _remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self,node):
        prev_end = self.tail.prev
        prev_end.next = node

        node.prev = prev_end
        node.next = self.tail

        self.tail.prev = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)