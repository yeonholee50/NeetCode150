# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        if greater or equal to predacessor, add to the list and increment counter
        """
        count = 0
        def dfs(root, predecessor):
            nonlocal count
            if root == None:
                return
            
            if predecessor <= root.val:
                count+=1
            predecessor = max(root.val, predecessor)
            dfs(root.left, predecessor)
            dfs(root.right, predecessor)
                
        dfs(root, -float('inf'))
        return count