class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(OpenN, CloseN):
            if OpenN == CloseN == n:
                res.append("".join(stack))
                return
            if OpenN < n:
                stack.append('(')
                backtrack(OpenN + 1, CloseN)
                stack.pop()
            if CloseN < OpenN:
                stack.append(')')
                backtrack(OpenN, CloseN + 1)
                stack.pop()
        backtrack(0, 0)
        return res