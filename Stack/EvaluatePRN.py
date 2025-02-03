class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    if num1 / num2 > 0:
                        stack.append(num1 // num2)
                    else:
                        stack.append(-1 * (abs(num1) // abs(num2)))
            
        return stack[0]