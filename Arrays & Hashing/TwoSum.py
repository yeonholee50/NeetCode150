class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in hm.keys():
                return [hm[num], i]
            else:
                hm[target - num] = i