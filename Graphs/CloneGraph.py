"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        hm = {}

        def dfs(node):
            if node in hm.keys():
                return hm[node]
            else:
                copy = Node(node.val)
                hm[node] = copy
                for neighbor in node.neighbors:
                    copy.neighbors.append(dfs(neighbor))
                return copy
        return dfs(node) if node else None