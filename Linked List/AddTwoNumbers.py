# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        head, curr = None, None
        curr1, curr2 = l1, l2
        carry = 0
        while curr1 and curr2:
            
            if head is None and curr is None:
                head = ListNode((curr1.val + curr2.val + carry)%10)
                carry = (curr1.val + curr2.val + carry) // 10
                curr = head
                curr1 = curr1.next
                curr2 = curr2.next
            elif curr1 is not None and curr2 is not None:
                curr.next = ListNode((curr1.val + curr2.val + carry)%10)
                carry = (curr1.val + curr2.val + carry) // 10
                curr1 = curr1.next
                curr2 = curr2.next
                curr = curr.next
        l = curr1 if curr1 is not None else curr2
        while l is not None:
            curr.next = ListNode((l.val + carry) % 10)
            carry = (l.val + carry) // 10
            curr = curr.next
            l = l.next
        if carry:
            curr.next = ListNode(carry)
        return head