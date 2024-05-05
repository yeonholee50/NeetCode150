class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summation = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in summation.keys():
                return [i, summation[num]]
            else:
                summation[target - num] = i