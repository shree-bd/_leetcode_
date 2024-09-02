# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev, curr = None, slow.next
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # Disconnect the first half and the second half
        slow.next = None
        
        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            # Save next pointers
            temp1, temp2 = first.next, second.next
            # Reorder pointers
            first.next = second
            second.next = temp1
            # Move to the next nodes
            first, second = temp1, temp2




                
        