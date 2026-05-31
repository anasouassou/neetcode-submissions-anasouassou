class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        sortedNums = sorted(nums)

        for i in range(len(sortedNums)):
            
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            
            left, right = i + 1, len(sortedNums) - 1
            currentTarget = sortedNums[i]
            
            while left < right:

                if sortedNums[left] + sortedNums[right] > -currentTarget:
                    right -= 1
                elif sortedNums[left] + sortedNums[right] < -currentTarget:
                    left += 1
                else:
                    res.append([currentTarget, sortedNums[left], sortedNums[right]])
                    right -= 1
                    left += 1
                    while sortedNums[left] == sortedNums[left - 1] and left < right:
                        left += 1
                    while sortedNums[right] == sortedNums[right + 1] and left < right:
                        right -= 1
        
        return res
