class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        if there's two 0s, than we return array of 0s
        if there's 1 0, than we put the product in that index and the rest is 0s
        """
        prod = 1
        res = [0] * len(nums)
        zero = False
        index = None
        for i in range(len(nums)):
            num = nums[i]
            if num == 0 and zero == True:
                return res
            elif num == 0:
                zero = True
                index = i
            else:
                prod*=num
        if zero == True:
            res[index] = prod
            return res

        for i in range(len(res)):
            res[i] = prod // nums[i]
        return res