class Solution:
    def check_time(self, piles, k, h):
        temp = 0
        for i in range(len(piles)):
            temp += math.ceil(piles[i]/k)
        return temp <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)

        while left < right: 

            mid = (left + right) // 2

            if self.check_time(piles, mid, h):
                right = mid
            else: 
                left = mid + 1

        return left
