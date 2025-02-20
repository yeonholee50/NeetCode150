# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        inorder traversal
        """

        ls = []

        def inorder(root):
            if root is None:
                return
            else:
                inorder(root.left)
                ls.append(root.val)
                inorder(root.right)
        inorder(root)

        p = -float('inf')
        for n in ls:
            if n <= p:
                return False
            p = n
        return True

        