# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Simplest solution is to construct a list an ensure that the left is always bigger than right subtree. or we can get a max min from each construction 
        of arr passed back. But that'll take too long
        """
        def inorder(node):
            if node == None:
                return []
            else:
                left_arr = inorder(node.left)
                right_arr = inorder(node.right)
                return left_arr + [node.val] + right_arr
        arr = inorder(root)
        if len(arr) == 1:
            return True
        else:
            i = 0
            j = 1
            while j < len(arr) and arr[j] > arr[i]:
                i+=1
                j+=1
            return j == len(arr)