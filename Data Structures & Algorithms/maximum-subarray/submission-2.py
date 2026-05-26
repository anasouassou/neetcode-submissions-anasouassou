class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        curSum = 0
        maxSum = nums[0]

        if len(nums) == 1:
            return nums[0]

        for r in range(len(nums)):
            curSum += nums[r]
            print('curSum: ', curSum)
            maxSum = max(maxSum, curSum) 
            if curSum < 0:
                l = r + 1
                curSum = 0
            print('maxSum: ', maxSum)
        print('final maxSum: ', maxSum)
        return maxSum