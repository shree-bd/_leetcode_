# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # if not headA or not headB:
        #     return None
        # # calculate lenght of both lists
        # lengthA, lengthB = 0,0
        # currA, currB = headA, headB

        # while currA != None:
        #     lengthA += 1
        #     currA = currA.next

        # while currB != None:
        #     lengthB += 1
        #     currB = currB.next
        
        # # Align the starting point of both lists
        # currA, currB = headA, headB
        # if lengthA > lengthB:
        #     for _ in range(lengthA - lengthB):
        #         currA = currA.next
        # else:
        #     for _ in range(lengthB - lengthA):
        #         currB = currB.next

        # # traverse both lists and find the intersection
        # while currA and currB:
        #     if currA==currB:
        #         return currA
        #     currA = currA.next
        #     currB = currB.next
        
        # return None
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1
            
        