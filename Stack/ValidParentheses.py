class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == '{' or p == '[' or p == '(':
                stack.append(p)
            else: 
                if len(stack) == 0:
                    return False
                open_p = stack.pop(-1)
                if (open_p == '{' and p != '}') or (open_p == '[' and p != ']') or (open_p == '(' and p != ')'):
                    return False

        return len(stack) == 0