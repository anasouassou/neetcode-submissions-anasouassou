class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxGain = 0

        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                currentGain = prices[r] - prices[l]
                maxGain = max(maxGain, currentGain)
            else:
                l = r
            print(l, ' ', r, ' ', maxGain)
        return maxGain