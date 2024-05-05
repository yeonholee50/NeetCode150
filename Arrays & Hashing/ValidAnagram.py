class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            hm = {}
            for i in range(len(s)):
                char_s = s[i]
                char_t = t[i]
                if char_s in hm.keys():
                    hm[char_s]+=1
                    if hm[char_s] == 0:
                        del hm[char_s]
                else:
                    hm[char_s] = 1
                if char_t in hm.keys():
                    hm[char_t]-=1
                    if hm[char_t] == 0:
                        del hm[char_t]
                else:
                    hm[char_t] = -1
            return len(hm.keys()) == 0