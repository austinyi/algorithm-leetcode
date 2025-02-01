# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(n), Space: O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find middle point (slow)
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse second half (slow)
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Check palindrome
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
