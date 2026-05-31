class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                return [min(i, seen[nums[i]]), max(i, seen[nums[i]])]
            seen[target-nums[i]] = i