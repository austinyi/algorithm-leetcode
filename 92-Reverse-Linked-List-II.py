# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        l, cur = dummy, head
        for i in range(left - 1):
            l = cur
            cur = cur.next

        prev = None
        for i in range(left - 1, right):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        l.next.next = cur
        l.next = prev

        return dummy.next

    
