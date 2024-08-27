class Solution:
    def numDecodings(self, s: str) -> int:
        """
        the only way its invalid is if the first character we read is 0 when going through s
        a bit like the house robbing problem i guess 
        """
        dp = {len(s): 1}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] =="0":
                return 0
            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                res+=dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)