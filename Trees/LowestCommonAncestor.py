# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        it's a Bst, so if it's a number in between when we traverse, then it must be that one
        """
        if root == None:
            return None
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p , q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        