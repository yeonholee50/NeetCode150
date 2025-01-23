class Solution:
    def isHappy(self, n: int) -> bool:
        
        if n == 1:
            return True
        num_set = set()
        while n not in num_set:
            num_set.add(n)
            dummy = 0
            while n != 0:
                p = n%10
                dummy+=(p**2)
                n = n // 10
            if dummy == 1:
                return True
            n = dummy

        return False