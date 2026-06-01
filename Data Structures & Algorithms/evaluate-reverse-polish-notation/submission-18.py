class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif token == '-':
                res = - stack.pop() + stack.pop()
                stack.append(res)
            elif token == '/':
                res = int((1/stack.pop())*stack.pop())
                stack.append(res)
            elif token == '*':
                res = stack.pop()*stack.pop()
                stack.append(res)
            else:
                stack.append(int(token))
            print(stack)
        return stack.pop()
