class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # if len(tokens) == 1:
        #     return int(tokens[-1])
        for i in tokens:

            if i in ('+'):
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif i in ('-'):
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            
            elif i in ('*'):
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)

            elif i in ('/'):
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))

            else:
                stack.append(int(i))
            
        return stack.pop()