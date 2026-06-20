class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        res = 0

        for i in range(len(nums)):
            current_res = 1
            if nums[i] - 1 not in hs:
                counter = 1
                while nums[i] + counter in hs:
                    current_res += 1
                    counter += 1
            res = max(res, current_res)

        return res