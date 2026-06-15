class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_profit = 0
        while left < right:
            profit = min(heights[left], heights[right])*(right-left)
            max_profit = max(max_profit, profit)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_profit