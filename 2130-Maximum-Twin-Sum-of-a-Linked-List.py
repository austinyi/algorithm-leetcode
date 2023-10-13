# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # Reverse second part
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        ans = 0
        while prev:
            ans = max(ans, prev.val + head.val)
            prev, head = prev.next, head.next

        return ans
        
