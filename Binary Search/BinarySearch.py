class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        i = 1

        while i < len(nums) and nums[i] < target:
            i*=2
        if i >= len(nums):
            i = len(nums) - 1
        while i > 0 and nums[i] > target:
            i-=1
        return i if nums[i] == target else -1
        