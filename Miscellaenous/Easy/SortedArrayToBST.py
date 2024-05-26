# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if len(nums) <= 0:
            return None
        else:
            median = nums[len(nums)//2]
            root = TreeNode(val=median) 
            root.left = self.sortedArrayToBST(nums[:len(nums)//2])
            root.right = self.sortedArrayToBST(nums[len(nums)//2+1:])
            return root
        """
        We can make make the median of each nums list be the root at that level
        basicaly recursion
        """