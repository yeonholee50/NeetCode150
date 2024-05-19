# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr is not None:
            stack.append(curr)
            curr = curr.next
        if len(stack) == 1:
            return None
        elif n == 1:
            stack[-n-1].next = None
        elif n == len(stack):
            return stack[1]
        else:
            stack[-n-1].next = stack[-n+1]
        return None if len(stack) == 0 else stack[0]
        