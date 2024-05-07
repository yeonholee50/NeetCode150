# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        basically test if it's an avl
        """
        return self.avl_traversal(root)[-1]
    
    """
    given node, we should return the node itself, the depth for upper recursive calculation, and a bool value saying that call is height balanced
    """
    def avl_traversal(self, root):
        if root == None:
            return root, 0, True
        else:
            root.left, left_depth, left_bool = self.avl_traversal(root.left)
            if left_bool == False:
                return root, left_depth, False
            root.right, right_depth, right_bool = self.avl_traversal(root.right)
            if right_bool == False:
                return root, right_depth, False
            if abs(right_depth - left_depth) > 1:
                return root, 0, False
            else:
                return root, max(left_depth, right_depth) + 1, True