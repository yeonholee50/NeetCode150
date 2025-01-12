class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = {}
        for i in range(len(s)):
            if s[i] in hm.keys():
                hm[s[i]]+=1
            else:
                hm[s[i]] = 1
            if hm[s[i]] == 0:
                del hm[s[i]]
            if t[i] in hm.keys():
                hm[t[i]]-=1
            else:
                hm[t[i]] = -1
            if hm[t[i]] == 0:
                del hm[t[i]]
        return True if len(hm.keys()) == 0 else False