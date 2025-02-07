class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        keep multi until you get nums[i] > nums[i * 2]
        """
        
        if len(nums) == 1 or nums[-1] > nums[0]:
            return nums[0]
        else:
            i = 1
            while i < len(nums) and nums[i] > nums[i//2]:
                i*=2
            if i >= len(nums):
                i = len(nums) - 1
            
            while i > 0 and nums[i] > nums[i - 1]:
                
                i-=1
            return nums[i]