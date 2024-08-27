class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        houses are arranged in circle so circular array.
        meaning if we choose to rob last house, we can't choose first
        and if we choose to rob first house, we can't choose last
        """
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        """
        we simulate robbing without first and without last or if there's onlt one, just do nums[0]
        """
    def helper(self, nums):
        rob1 = 0
        rob2 = 0
        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return max(rob1, rob2)