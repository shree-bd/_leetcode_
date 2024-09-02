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
        # find middle
        slow, fast = head, head.next
        while fast and fast.next is not None:
            slow = slow.next                               # slow shifts one place 
            fast = fast.next.next                          # fast shifts two place

        # reverse second half
        second = slow.next
        prev = slow.next = None

        while second is not None:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge two halfs
        first, second = head, prev
        while second is not None:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2






                
        