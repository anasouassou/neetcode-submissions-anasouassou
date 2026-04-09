class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []

        for i in tokens:
            if i == '+':
                self.stack.append(int(self.stack.pop()) + int(self.stack.pop()))
            
            elif i == '-':
                a, b = int(self.stack.pop()), int(self.stack.pop())
                self.stack.append(b-a)

            elif  i == '*':
                a, b = int(self.stack.pop()), int(self.stack.pop())
                self.stack.append(b*a)
            
            elif  i == '/':
                a, b = int(self.stack.pop()), int(self.stack.pop())
                self.stack.append(int(b/a))

            else:
                self.stack.append(int(i))

        return self.stack[0]