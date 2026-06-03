class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        currentProfit, highestProfit = 0, 0
        left = 0
        minPrice = prices[left]

        for right in range(len(prices)):
            minPrice = min(minPrice, prices[right])
            currentProfit = prices[right]-minPrice
            highestProfit = max(currentProfit, highestProfit)
            print(prices[right], minPrice, currentProfit)

        return highestProfit
