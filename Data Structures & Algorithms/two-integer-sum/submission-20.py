class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hs:
                return [hs[complement], i]
            hs[num] = i