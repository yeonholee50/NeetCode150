class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        letters = set()
        
        l, r = 0, 1
        letters.add(s[l])
        maximum = 1
        while r < len(s):
            if s[r] in letters:
                
                l+=1
                letters = set()
                letters.add(s[l])
                r = l + 1
            else:
                letters.add(s[r])
                r+=1
                
        
            maximum = max(maximum, r - l)
        
        
        return maximum
