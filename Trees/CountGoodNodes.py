# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def pre_order(node, greatest):
            nonlocal count
            if node is None:
                return
            else:
                if node.val >= greatest:
                    count+=1

                greatest = max(greatest, node.val)

                pre_order(node.left, greatest)
                pre_order(node.right, greatest)
        pre_order(root, root.val)
        return count