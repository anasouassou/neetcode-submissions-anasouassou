class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        everything = sorted([(p, s) for p,s in zip(position, speed)], reverse=True)
        for p, s in everything:
            time = float((target-p))/s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)