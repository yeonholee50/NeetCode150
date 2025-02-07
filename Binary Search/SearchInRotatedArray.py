class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def findMin(nums: List[int]) -> int:
            """
            keep multi until you get nums[i] > nums[i * 2]
            """
            
            if len(nums) == 1 or nums[-1] > nums[0]:
                return 0
            else:
                i = 1
                while i < len(nums) and nums[i] > nums[i//2]:
                    i*=2
                if i >= len(nums):
                    i = len(nums) - 1
                
                while i > 0 and nums[i] > nums[i - 1]:
                    
                    i-=1
                return i
        j = findMin(nums)
        arr = nums[j:] + nums[:j]
        if len(arr) == 1 or arr[0] == target:
            return j if arr[0] == target else -1
        else:
            i = 1
            while i < len(arr) and arr[i] < target:
                i*=2
            if i >= len(arr):
                i = len(arr) - 1
            while i > 0 and arr[i] > target:
                i-=1
            return (j + i) % len(arr) if target == arr[i] else -1