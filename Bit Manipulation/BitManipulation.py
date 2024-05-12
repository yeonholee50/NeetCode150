class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = 0
        for i in range(len(nums)):
            num = nums[i] ^ num ^ i
        num = num ^ len(nums)
        return num