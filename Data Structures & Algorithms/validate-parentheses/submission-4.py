class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        stack = []

        openToClose = {')':'(', ']':'[', '}':'{'}
        
        for i in s:
            print(stack)
            if i not in openToClose:
                stack.append(i)
            else:
                if not stack:
                    return False
                elif stack.pop() != openToClose[i]:
                    return False
        return len(stack) == 0
        