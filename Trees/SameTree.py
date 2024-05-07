# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None and q != None:
            return False
        elif p != None and q == None:
            return False
        else:
            """
            reason to go preorder is for efficiency. if val is not same in upper recursion, there is no reason to 
            go down the entire tree
            """
            if p.val != q.val:
                return False
            left_bool = self.isSameTree(p.left, q.left)
            if left_bool == False:
                return False
            else:
                return self.isSameTree(p.right, q.right)