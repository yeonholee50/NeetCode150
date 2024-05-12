class Solution:
    def reverseBits(self, n: int) -> int:
        bits = [0] * 32
        for i in range(len(bits)):
            bits[i] = n % 2
            n = n // 2
        res = 0
        counter = 1
        bits.reverse()
        for bit in bits:
            res+=(bit*counter)
            counter*=2
        return res