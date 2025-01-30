class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r and numbers[r] + numbers[l] != target:
            summation = numbers[r] + numbers[l]
            if summation > target:
                r-=1
            elif summation < target:
                l+=1
        return [l + 1, r + 1]