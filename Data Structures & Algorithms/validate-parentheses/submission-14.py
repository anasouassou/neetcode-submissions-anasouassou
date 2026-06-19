class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        openToClose = {
            "[":"]",
            "(":")",
            "{":"}"
        }

        for i in s:
            if i in openToClose:
                stack.append(i)
            elif not stack or openToClose[stack.pop()] != i:
                return False
        
        return len(stack) == 0