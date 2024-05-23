# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        we can do a dfs and stop when list is at k capacity since it's a bst
        code repetition is never good but this was a simple way to break out of doing extra recursion
        """
        res = []
        def dfs(root):
            if root == None:
                return
            if len(res) == k:
                return
            dfs(root.left)
            if len(res) == k:
                return
            res.append(root.val)
            if len(res) == k:
                return
            dfs(root.right)

        dfs(root)
        return res[-1]