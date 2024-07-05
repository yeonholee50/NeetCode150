# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        we can run inorder algo and then go through list
        """
        arr = []
        def inorder(root):
            if root == None:
                return 
            else:
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)
        inorder(root)
        if len(arr) < 2:
            return True
        else:
            i, j = 0, 1
            while j < len(arr):
                if arr[i] >= arr[j]:
                    return False
                i+=1
                j+=1
            return True

        