class Solution:
    def isValid(self, s: str) -> bool:

        closeToOpen = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for i in range(len(s)):
            
            if s[i] not in closeToOpen:
                stack.append(s[i])
            else:
                if not stack or closeToOpen[s[i]] != stack[-1]:
                    return False
                stack.pop()


        return len(stack) == 0

            
