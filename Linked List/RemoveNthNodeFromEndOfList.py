# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        q = []
        curr = head
        while curr:
            q.append(curr)
            curr = curr.next
        index = len(q) - n
        if index - 1 < 0:
            return head.next
        else:
            prev = q[index - 1]
            prev.next = q[index].next
            return head
