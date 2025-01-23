class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = None
        for num in nums:
            if res is None:
                res = num
            else:
                res = res ^ num
        return res