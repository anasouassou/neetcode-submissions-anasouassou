class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums_set = set(nums)
        res = 1

        for i in range(len(nums)):
            if nums[i]-1 not in nums_set:
                temp = 1
                while nums[i] + temp in nums_set and temp < len(nums):
                    temp += 1
                
                res = max(res, temp)
        
        return res
        
