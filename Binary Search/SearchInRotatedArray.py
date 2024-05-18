class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        i = 1
        while i < len(nums) and nums[i] > nums[i//2]:
            i*=2
        if i >= len(nums):
            i = len(nums) - 1
        while i > 0 and nums[i - 1] < nums[i]:
            i-=1
        """
        modified rotated i so we know i is at the min
        """
        counter = i
        if target <= nums[-1]:
            arr = nums[i:]
            if len(arr) == 0:
                return -1
            if len(arr) == 1:
                return counter if arr[0] == target else -1
            if target == nums[0]:
                return counter
            i = 1
            while i < len(arr) and arr[i] < target:
                i*=2
            if i >= len(arr):
                i = len(arr) - 1
            while i > 0 and arr[i] > target:
                i-=1
            return i + counter if arr[i] == target else -1
        else:
            arr = nums[0:i]
            if len(arr) == 0:
                return -1
            if len(arr) == 1:
                return 0 if arr[0] == target else -1
            if target == nums[0]:
                return 0
            i = 1
            while i < len(arr) and arr[i] < target:
                i*=2
            if i >= len(arr):
                i = len(arr) - 1
            while i > 0 and arr[i] > target:
                i-=1
            
            return i if arr[i] == target else -1