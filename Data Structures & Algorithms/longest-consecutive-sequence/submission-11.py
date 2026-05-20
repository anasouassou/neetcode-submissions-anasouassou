class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i]-1 not in seen:
                print(nums[i], 'is a start of a sequence !')
                j = 1
                while nums[i]+j in seen:
                    j+=1
                res = max(res, j)
        return res