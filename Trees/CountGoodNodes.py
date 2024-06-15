# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Let's construct a list. We append node to list if it's a good node
        """
        count = 0

        def dfs(node, arr):
            nonlocal count
            if node == None:
                return
            elif len(arr) == 0:
                count+=1    
                dfs(node.left, arr + [node.val])
                dfs(node.right, arr + [node.val])
            else:
                if node.val >= arr[-1]:
                    count+=1
                    dfs(node.left, arr + [node.val])
                    dfs(node.right, arr + [node.val])
                else:
                    dfs(node.left, arr)
                    dfs(node.right, arr)
            

        dfs(root, [])
        return count