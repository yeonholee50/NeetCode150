class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                t = stack.pop(-1)
                if t == '[' and c != ']':
                    return False
                elif t == '(' and c != ')':
                    return False
                elif t == '{' and c != '}':
                    return False
        return len(stack) == 0
                