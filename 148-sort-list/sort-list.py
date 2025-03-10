# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        #split the list into two halfs
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.mergeSort(left, right)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next # one step
            fast = fast.next.next # two steps
        return slow

    
    def mergeSort(self, l1, l2):
        tail = dummy = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

            tail.next = l1 if l1 else l2
        return dummy.next



        