# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        while curr:
            curr.val = stack.pop()
            curr = curr.next
        return head

        