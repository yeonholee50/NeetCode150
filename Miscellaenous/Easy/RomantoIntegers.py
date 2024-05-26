class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500, 
            'M': 1000,
        }
        res = 0
        i = 0
        while i < len(s):
            c = s[i]
            if i != len(s) - 1:
                """
                we can check next
                """
                n = s[i + 1]
                if c == 'I' and (n == "V" or n == "X"):
                    res+=(roman_int[n] - roman_int[c])
                    i+=1
                elif c == 'X' and (n == "L" or n == "C"):
                    res+=(roman_int[n] - roman_int[c])
                    i+=1
                elif c == 'C' and (n == "D" or n == "M"):
                    res+=(roman_int[n] - roman_int[c])
                    i+=1
                else:
                    res+=roman_int[c]
                
            else:
                res+=roman_int[c]
            i+=1
        return res