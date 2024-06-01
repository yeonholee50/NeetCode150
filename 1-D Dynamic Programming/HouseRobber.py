class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        """
        rob2 is choose not to rob at current
        but you can still rob if you want
        """
        
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        return max(rob1, rob2)