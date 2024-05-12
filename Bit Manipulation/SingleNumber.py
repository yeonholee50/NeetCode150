class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = None
        for num in nums:
            if number == None:
                number = num
            else:
                number = number ^ num
        return number