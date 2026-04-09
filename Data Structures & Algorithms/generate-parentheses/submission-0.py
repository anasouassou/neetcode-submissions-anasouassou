class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(leftcount, rightcount):

            if leftcount == rightcount == n:
                res.append(''.join(stack))
                return
            
            if leftcount < n:
                stack.append('(')
                backtrack(leftcount+1, rightcount)
                stack.pop()

            if rightcount < leftcount:
                stack.append(')')
                backtrack(leftcount, rightcount+1)
                stack.pop()
            
        backtrack(0,0)
        return res
            