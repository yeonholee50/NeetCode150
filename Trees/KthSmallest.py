# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        we can do an inorder traversal.
        but an early exit inorder traversal
        """

        def inorder(node):
            if node == None:
                return []
            else:
                left_arr = inorder(node.left) + [node.val]
                if len(left_arr) >= k:
                    return left_arr
                else:
                    return left_arr + inorder(node.right)


        arr = inorder(root)
        if len(arr) <= k:
            return arr[-1]
        else:
            return arr[k - 1]
