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
        curr = head
        q = []
        while curr:
            copy = curr
            curr = curr.next
            copy.next = None
            q.append(copy)
        first = True
        while q:
            if first == True:
                first = False
                node = q.pop(0)
                if q:
                    node.next = q[-1]
                else:
                    return
            else:
                first = True
                node = q.pop(-1)
                if q:
                    node.next = q[0]
                else:
                    return