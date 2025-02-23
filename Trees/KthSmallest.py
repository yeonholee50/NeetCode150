# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        inorder but we go for early termination
        """
        ls = []
        def inorder(node):
            if node is None:
                return
            else:
                inorder(node.left)
                ls.append(node.val)
                if len(ls) == k:
                    return
                inorder(node.right)
        inorder(root)
        return ls[k - 1]