# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        not always guranteed we will use the right msot so we should do level order and append what's at the end
        """
        res, q = [], []

        if root:
            q.append(root)

        while q:
            level = []
            len_q = len(q)
            for i in range(len_q):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level[-1])
        return res