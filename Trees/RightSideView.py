# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
            res = []
            if root is None:
                return res
            q = [[root, 0]]

            while q:
                node, depth = q[0]
                depth+=1
                level = []
                for i in range(len(q)):
                    node, _ = q.pop(0)
                    level.append(node.val)
                    if node.left is not None:
                        q.append([node.left, depth])
                    if node.right is not None:
                        q.append([node.right, depth])
                res.append(level)
            return res
        ls = levelOrder(root)
        return [ls[i][-1] for i in range(len(ls))]