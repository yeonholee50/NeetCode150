"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        elif head in self.map:
            return self.map[head]
        else:

            copy = Node(head.val)
            self.map[head] = copy
            copy.next = self.copyRandomList(head.next)
            if head.random in self.map:
                copy.random = self.map[head.random]
            return copy