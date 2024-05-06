# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        can use tortoise hare algorithm
        """
        if head == None:
            return False
        h = head
        t = head.next
        while t:
            if h == t:
                return True
            h = h.next
            t = t.next
            if t == None:
                return False
            t = t.next
        return False