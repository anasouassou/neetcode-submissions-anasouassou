class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target-nums[i] in set(nums) and i != nums.index(target-nums[i]):
                if i > nums.index(target-nums[i]):
                    return [nums.index(target-nums[i]), i]
                return [i, nums.index(target-nums[i])]
