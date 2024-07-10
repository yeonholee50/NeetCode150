class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digits_to_char = {
            "1": None,
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i, current):
            if len(current) == len(digits):
                res.append(current)
                return
            else:
                for c in digits_to_char[digits[i]]:
                    dfs(i + 1, current + c)
        if digits:
            dfs(0, "")
        return res
