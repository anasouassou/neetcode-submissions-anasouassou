class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1] :
                print(t, '---', stack)
                couple = stack.pop()
                res[couple[0]] = i-couple[0]
            print('#####')
            stack.append((i, t))

        return res