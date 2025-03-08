# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
                
        if not lists:
            return None        

        while len(lists) > 1:
            result = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                result.append(self.merge(list1, list2))
            lists = result
        
        return lists[0]

    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next  # Move the tail pointer

        tail.next = l1 if l1 else l2  # Attach the remaining part of the list

        return dummy.next  # Return the merged list, starting from dummy.next







            

























    #     if not lists or len(lists) == 0:
    #         return None

    #     while len(lists) > 1:
    #         mergedLists = []

    #         for i in range(0, len(lists), 2):
    #             l1 = lists[i]
    #             l2 = lists[i+1] if (i+1) < len(lists) else None
    #             mergedLists.append(self.mergeList(l1, l2))
            
    #         lists = mergedLists  # Reduce the list size iteratively
        
    #     return lists[0]  

    # def mergeList(self, l1, l2):
    #     dummy = ListNode()
    #     tail = dummy

    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             tail.next = l1
    #             l1 = l1.next
    #         else:
    #             tail.next = l2
    #             l2 = l2.next
    #         tail = tail.next  # Move the tail pointer

    #     tail.next = l1 if l1 else l2  # Attach the remaining part of the list

    #     return dummy.next  # Return the merged list, starting from dummy.next

# Time Complexity: O(N log K)
# Space Complexity: O(1)


# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         min_heap = []
        
#         # Push the first node of each list into the heap
#         for i, l in enumerate(lists):
#             if l:
#                 heappush(min_heap, (l.val, i, l))  # Store (value, index, node)

#         dummy = ListNode()
#         tail = dummy

#         while min_heap:
#             val, i, node = heappop(min_heap)
#             tail.next = node
#             tail = tail.next

#             if node.next:
#                 heappush(min_heap, (node.next.val, i, node.next))  # Push next node

#         return dummy.next