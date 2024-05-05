class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        s.strip()
        r = len(s) - 1

        while r > l:
            while r > l and s[r].isalnum() == False:
                r-=1
            if r == l:
                break
            while r > l and s[l].isalnum() == False:
                l+=1
            if r == l:
                break
            if s[r].lower() != s[l].lower():
                return False
            else:
                r-=1
                l+=1


        return True
        