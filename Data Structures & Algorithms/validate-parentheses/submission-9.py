class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {
            '{':'}',
            '[':']',
            '(':')'
        }
        stack = []
        for i in s:
            if i in openToClose:
                stack.append(i)
            else:
                if not stack:
                    return False
                elif i != openToClose[stack.pop()]:
                    return False
        return len(stack)==0
