class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_index = None

        product = 1
        for i in range(len(nums)):
            num = nums[i]
            if num == 0 and zero_index is not None:
                return [0] * len(nums)
            elif num == 0 and zero_index is None:
                zero_index = i
            else:
                product*=num
        if zero_index is not None:
            product_array = [0] * len(nums)
            product_array[zero_index] = product
            return product_array
        else:
            product_array = [int(product//num) for num in nums]
            return product_array