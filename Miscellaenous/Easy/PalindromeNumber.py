class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        mapping = {
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            0: "0",
        }
        """
        
        if x < 0:
            return False
        
        prefix = []
        
        
        while x != 0:
            n = x % 10
            prefix.append(n)
            
            
            
            x = x // 10
        print(prefix)
        return prefix[::-1] == prefix