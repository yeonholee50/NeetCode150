class Solution:
    def climbStairs(self, n: int) -> int:
        """
        haven't seen dp in a while, but essentially,
        find n-1 problem solutio nand then n-2 solution
        n depends on n-1 and n-2 problem
        """
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2
