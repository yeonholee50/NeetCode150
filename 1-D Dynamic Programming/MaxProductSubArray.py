class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n)/O(1) : Time/Memory
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            temp = curMax * num

            curMax = max(num * curMax, num * curMin, num)
            curMin = min(temp, num * curMin, num)
            
            res = max(res, curMax)
        return res