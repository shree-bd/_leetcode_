# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True  # Single node or empty list is always a palindrome

        # Step 1: Find the middle using slow & fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # Step 3: Compare first half with reversed second half
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
        
# Time Complexity: O(N)
# Space Complexity: O(1)

        """
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True

# Time Complexity: O(N)
# Space Complexity: O(N)        
        
        """
            

        