# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        We can construct a list where there is valid node. 
        """
        counter = 0

        def dfs(node, arr):
            nonlocal counter
            if node == None:
                return
            else:
                if len(arr) == 0:
                    counter+=1
                    dfs(node.left, arr + [node.val])
                    dfs(node.right, arr + [node.val])
                else:
                    """
                    arr is not empty
                    """
                    if node.val >= arr[-1]:
                        counter+=1
                        dfs(node.left, arr + [node.val])
                        dfs(node.right, arr + [node.val])
                    else:
                        dfs(node.left, arr)
                        dfs(node.right, arr)



        dfs(root, [])
        return counter