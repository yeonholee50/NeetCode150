class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 1
        while carry == 1 and i >= 0:
            if digits[i] + carry >= 10:
                carry = 1
                digits[i] = (digits[i] + carry)%10
            else:
                digits[i]+=carry
                carry = 0
            i-=1
        if carry == 1:
            digits.insert(0, 1)
        return digits