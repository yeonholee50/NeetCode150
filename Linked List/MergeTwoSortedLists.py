# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list2 == None:
            return list1
        elif list1 == None:
            return list2
        else:
            curr1 = list1
            curr2 = list2
            curr = None
            if curr1.val > curr2.val:
                curr = ListNode(curr2.val, None)
                curr2 = curr2.next
            else:
                curr = ListNode(curr1.val, None)
                curr1 = curr1.next
            head = curr
            while curr1 and curr2:
                dummy = None
                if curr1.val > curr2.val:
                    dummy = ListNode(curr2.val, None)
                    curr2 = curr2.next
                else:
                    dummy = ListNode(curr1.val, None)
                    curr1 = curr1.next 
                curr.next = dummy
                curr = curr.next
            if curr1:
                curr.next = curr1
            elif curr2:
                curr.next = curr2

            return head

        