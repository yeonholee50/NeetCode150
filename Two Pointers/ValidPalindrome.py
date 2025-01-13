class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        if len(s) == 0:
            return True
        l = 0
        r = len(s) - 1

        while r > l:
            while l < len(s) and not (ord(s[l]) >= 97 and ord(s[l]) <= 122) and not (ord(s[l]) >= 48 and ord(s[l]) <= 57):
                l+=1
            while r >= 0 and not (ord(s[r]) >= 97 and ord(s[r]) <= 122) and not (ord(s[r]) >= 48 and ord(s[r]) <= 57):
                r-=1
            if r <= l:
                return True
            if s[r] != s[l]:
                return False
            r-=1
            l+=1
            
        return True
        