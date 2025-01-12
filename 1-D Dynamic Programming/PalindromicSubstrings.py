class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        
        def helper(l, r, s):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res.append(s[l:r+1])
                l-=1
                r+=1
        for i in range(len(s)):
            #odd
            helper(i, i, s)
            #even
            helper(i, i + 1, s)
        return len(res)