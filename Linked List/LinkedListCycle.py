# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        t = head
        h = head.next

        while h is not None:
            t = t.next
            h = h.next
            if h is None:
                return False
            h = h.next
            if h is None:
                return False
            if h == t:
                return True
        return False