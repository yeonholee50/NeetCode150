# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        we can pass on left and right node subtree if true. if false, we propage false value. if true is returned, compare curre node with left subtree max -> should be less than curr.val and min of right subtree -> should be greater than curr node.val
        if so, append to our list which is left subtree lsit + right sub tree lsit + curr.val and then pass it back with a true sayign out current recursion call passed - might need to make separate function

        """
        return self.valid_bst_traversal(root)[-1]
        
    def valid_bst_traversal(self, root):
        if root == None:
            return [], True
        else:
            left_arr, left_bool = self.valid_bst_traversal(root.left)
            if left_bool == False:
                return left_arr, False
            right_arr, right_bool = self.valid_bst_traversal(root.right)
            if right_bool == False:
                return right_arr, False
            if len(left_arr) != 0 and max(left_arr) >= root.val:
                return [], False
            if len(right_arr) != 0 and min(right_arr) <= root.val:
                return [], False
            """
            now valid
            """ 
            res = left_arr + [root.val] + right_arr
            return res, True