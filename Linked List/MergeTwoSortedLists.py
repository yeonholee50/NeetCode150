# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        curr1 = list1
        curr2 = list2

        curr = ListNode()
        head = curr
        

        while curr1 and curr2:
            if curr1.val >= curr2.val:
                curr.val = curr2.val
                curr2 = curr2.next
            elif curr1.val < curr2.val:
                curr.val = curr1.val
                curr1 = curr1.next

            if curr1 and curr2:
                curr.next = ListNode()
                curr = curr.next
        if curr1:
            curr.next = curr1
        elif curr2:
            curr.next = curr2
        return head