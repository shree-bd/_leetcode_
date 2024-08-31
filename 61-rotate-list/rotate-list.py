# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # First, determine the length of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Normalize k to be within the range of the length
        k %= length
        if k == 0:
            return head

        # Initialize two pointers
        slow = fast = head

        # Move fast pointer k steps ahead
        for _ in range(k):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next

        # slow.next is the new head after rotation
        new_head = slow.next
        slow.next = None  # Break the link to form the new end of the list
        fast.next = head  # Connect the old tail to the old head

        return new_head