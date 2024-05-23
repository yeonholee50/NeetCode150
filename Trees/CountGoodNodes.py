# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        we could consturct a list from root to there. if it's greatter of equal, then we pass back length and current arr
        if it's less that, we skip
        made big improvements from the max method because max is O(n) while if we just care about greater than or equal to and append to the
        end of the lsit, that's the only comparison we have to make. runtime is now 70%
        """
        counter = 0
        def post_order_traverse(root , root_list):
            nonlocal counter
            if root == None:
                return
            if len(root_list) == 0 or root.val >= root_list[-1]:
                counter+=1
                post_order_traverse(root.left, root_list + [root.val]) 
                post_order_traverse(root.right, root_list + [root.val])
            else:
                post_order_traverse(root.left, root_list) 
                post_order_traverse(root.right, root_list)
            

        post_order_traverse(root, [])
        return counter