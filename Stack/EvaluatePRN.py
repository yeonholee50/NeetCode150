class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token != "+" and token != "-" and token != "*" and token != "/":
                stack.append(int(token))
            else:
                if token == "+":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num1 + num2)
                elif token == "-":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 - num2)
                elif token == "*":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num1 * num2)
                elif token == "/":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    
                    if num1 * num2 >= 0:
                        stack.append(abs(num1)//abs(num2))
                    else:
                        stack.append(-(abs(num1)//abs(num2)))
                
            
        return stack[0]