# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        we can do an inorder and when the arr is k filled, then we can return
        """
        arr = []

        def inorder(root):
            if root == None:
                return
            if len(arr) == k:
                return
            else:
                inorder(root.left)
                if len(arr) == k:
                    return
                arr.append(root.val)
                if len(arr) == k:
                    return
                inorder(root.right)
        inorder(root)
        return arr[k - 1] if len(arr) >= k else arr[-1]
