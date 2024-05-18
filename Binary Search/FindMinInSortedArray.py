class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        we can do a bin search
        """
        if len(nums) == 1 or nums[-1] > nums[0]:
            return nums[0]
        i = 1
        while i < len(nums) and nums[i] > nums[i//2]:
            i*=2
        if i >= len(nums):
            i = len(nums) - 1
        while i > 0 and nums[i - 1] < nums[i]:
            i-=1
        return nums[i]