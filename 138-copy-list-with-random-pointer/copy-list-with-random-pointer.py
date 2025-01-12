# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Using Interweaving Approach <<<<<<<<<<<<<<<<<<<<<<<<<<<
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Interweave the copied nodes with the original nodes
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # Step 2: Assign random pointers for the copied nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the original and copied lists
        original = head
        copy = head.next
        copy_head = copy

        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next

        return copy_head
            





# Time complexity:  O(n)
# Space Complexity: O(1)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Using Opimized One Pass Approach <<<<<<<<<<<<<<<<<<<<<<<<<<<

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # hashmap to store mapping from org nodes to their corresponding copied nodes
        old_to_new = {}


        # Helper function 
        def get_cloned(node):
            if not node:
                return None
            
            if node not in old_to_new:
                # If not yet created, create and store the new node
                old_to_new[node] = Node(node.val)

            return old_to_new[node]

        # Start iterating through the original list
        curr = head
        while curr:
            copied_node = get_cloned(curr)

            copied_node.next = get_cloned(curr.next)
            copied_node.random = get_cloned(curr.random)

            # Move to the next node
            curr = curr.next

        # return the head of the copied list
        return old_to_new[head]
"""

# Time complexity:  O(n)
# Space Complexity: O(n)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Using Two Passes Approach <<<<<<<<<<<<<<<<<<<<<<<<<<<


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        # First pass: Create all nodes and map them
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Second Pass : Asssign next and random pointers
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next

        
        return old_to_new[head]
"""

# Time complexity:  O(n)
# Space Complexity: O(n)
