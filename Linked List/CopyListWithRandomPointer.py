"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        hm = {}
        hm[None] = None 
        curr = head
        while curr:
            copy = Node(curr.val)
            hm[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = hm[curr]
            copy.next = hm[curr.next]
            copy.random = hm[curr.random]
            curr = curr.next
        return hm[head]
