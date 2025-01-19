# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return self.avl_traversal(root)[0]


    def avl_traversal(self, root: Optional[TreeNode]):
        if root is None:
            return True, 0
        else:
            left_bool, left_depth = self.avl_traversal(root.left)
            if left_bool == False:
                return False, 0
            right_bool, right_depth = self.avl_traversal(root.right)
            if right_bool == False:
                return False, 0
            if abs(right_depth - left_depth) > 1:
                return False, 0
            else:
                return True, max(right_depth, left_depth) + 1