# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        
        dummy = cur = ListNode()
        i = 1
        while head:
            if i != length - n + 1:
                cur.next = head
                cur = cur.next
                head = head.next
            else:
                head = head.next
            i += 1
        if n == 1:
            cur.next = None
        return dummy.next

# # https://github.com/neetcode-gh/leetcode/blob/main/python/0019-remove-nth-node-from-end-of-list.py
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         dummy = ListNode(0, head)
#         left = dummy
#         right = head

#         while n > 0:
#             right = right.next
#             n -= 1

#         while right:
#             left = left.next
#             right = right.next

#         # delete
#         left.next = left.next.next
#         return dummy.next
