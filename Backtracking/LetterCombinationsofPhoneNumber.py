class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        str_to_char = {
            "1": None,
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": "_",
        }
        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            else:
                for c in str_to_char[digits[i]]:
                    backtrack(i + 1, currStr + c)
                    

        if digits:
            backtrack(0, "")
        return res
