# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        bascially level order but we only focus on right side and append that to res
        """
        res = []
        queue = []
        if root:
            queue.append(root)

        while queue:
            val = []

            for i in range(len(queue)):
                node = queue.pop(0)
                val.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            res.append(val[-1])
        return res