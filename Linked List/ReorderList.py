# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = []
        curr = head
        while curr:
            q.append(curr)
            prev = curr
            curr = curr.next
            prev.next = None
        curr = None
        first = True
        while q:
            if curr is None:
                first = False
                curr = q.pop(0)
            elif first is True:
                first = False
                curr.next = q.pop(0)
                curr = curr.next
            else:
                first = True
                curr.next = q.pop(-1)
                curr = curr.next
