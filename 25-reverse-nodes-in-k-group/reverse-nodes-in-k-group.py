# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # dummy node to handle edge cases
        groupPrev = dummy   # pointer to the node before the current group

        while True:
            # find the kth node in the current group
            kth = self.getKth(groupPrev, k)
            if not kth: # if there are fewer than k nods left, exit loop
                break
            groupNext = kth.next   # pointer to next group's first node

            #reverse group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next       # Return new head

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


# Time Complexity: O(N)
# Space Complexity: O(1)


        
        