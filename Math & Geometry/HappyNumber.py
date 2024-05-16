class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()

        while n not in nums:
            nums.add(n)
            temp = 0
            while n != 0:
                temp+=((n % 10) * (n % 10))
                n = n // 10
            n = temp
            if n == 1:
                return True
        return False