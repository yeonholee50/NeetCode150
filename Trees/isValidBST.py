# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        best idea is to ensure that the left subtree is always less than root. right subtree is always bigger than root. 
        we can construct a list using inorder and ensure that the list is inorder
        """
        
        def inorder(node):
            if node == None:
                return []
            else:
                return inorder(node.left) + [node.val] + inorder(node.right)
        arr = inorder(root)

        if len(arr) == 1:
            return True
        else:
            i = 0
            j = 1
            while j < len(arr):
                if arr[i] >= arr[j]:
                    return False
                i+=1
                j+=1
            return True

        