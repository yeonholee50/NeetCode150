class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            summation = digits[i] + carry
            if summation > 9:
                carry = 1
                res.insert(0, summation%10)
            else:
                carry = 0
                res.insert(0, summation)
                res = digits[0:i] + res
                return res
        if carry == 1:
            res.insert(0, 1)
        return res
            