class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]

        for (i, t) in enumerate(temperatures):
            if stack and t > stack[-1][1]:
                print(f"at {i}, {t}: ", stack)
                while stack and t > stack[-1][1]:
                    element = stack.pop()
                    res[element[0]] = i - element[0]
            stack.append((i, t))
        
        return res