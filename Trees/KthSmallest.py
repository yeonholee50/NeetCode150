# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        we can do a dfs and stop when lsit is at k capacity since it's a bst
        we construct an inorder until list is at capacity
        """
        res = []

        def dfs(root):
            nonlocal res
            if root == None:
                return
            elif len(res) >= k:
                return
            else:
                dfs(root.left)
                if len(res) >= k:
                    return 
                res = res + [root.val]
                if len(res) >= k:
                    return
                dfs(root.right)
        dfs(root)
        return res[-1] if len(res) < k else res[k-1]
