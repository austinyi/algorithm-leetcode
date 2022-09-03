# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left, right = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        '''
        if not l1:
            return l2
        elif not l2:
            return l1
        '''

        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l2.next, l1)
            return l2
