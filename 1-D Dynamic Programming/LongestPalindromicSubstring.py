class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        consider each character as center and expand outwards and it's O(n^2)
        """
        res = ""
        resLen = 0

        def getLongest(l, r, s):
            nonlocal res
            nonlocal resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l-=1
                r+=1

        for i in range(len(s)):
            c = s[i]
            #odd length
            getLongest(i, i, s)
            #even length
            getLongest(i, i + 1, s)
        return res