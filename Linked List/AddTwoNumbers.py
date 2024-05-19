# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = l1
        curr2 = l2
        carry = 0
        res = None
        if curr1.val + curr2.val >= 10:
            carry = 1
            res = ListNode((curr1.val + curr2.val)%10, None)
        else:
            res = ListNode(curr1.val + curr2.val, None)
        head = res
        curr1 = curr1.next
        curr2 = curr2.next
        while curr1 and curr2:
            next_res = ListNode()
            if curr1.val + curr2.val + carry >= 10:
                next_res.val = (curr1.val + curr2.val + carry)%10
                carry = 1
            else:
                next_res.val = curr1.val + curr2.val + carry
                carry = 0
            res.next = next_res
            res = res.next
            curr1 = curr1.next
            curr2 = curr2.next
        if not curr1 and not curr2 and carry:
            res.next = ListNode(carry, None)
            return head
        while curr1:
            next_res = ListNode()
            if curr1.val + carry >= 10:
                next_res.val = (curr1.val + carry)%10
                carry = 1
            else:
                next_res.val = curr1.val + carry
                carry = 0
            res.next = next_res
            res = res.next
            curr1 = curr1.next
            if carry == 0:
                res.next = curr1
            elif curr1 == None and carry == 1:
                res.next = ListNode(carry, None)
        while curr2:
            next_res = ListNode()
            if curr2.val + carry >= 10:
                next_res.val = (curr2.val + carry)%10
                carry = 1
            else:
                next_res.val = curr2.val + carry
                carry = 0
            res.next = next_res
            res = res.next
            curr2 = curr2.next
            if carry == 0:
                res.next = curr2
            elif curr2 == None and carry == 1:
                res.next = ListNode(carry, None)
        return head