class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        hs = set(nums)
        res = 1
        for i in range(len(nums)):
            current_length = 1
            if nums[i]-1 not in hs:
                j = 1
                while nums[i]+j in hs:
                    current_length += 1
                    j += 1
                res = max(res, current_length)
        return res
