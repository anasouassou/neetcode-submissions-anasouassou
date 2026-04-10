class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        first = [1]*len(nums)
        second = [1]*len(nums)
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            first[i] = prefix
            prefix *= nums[i]
        print(first)
    
        for i in range(len(nums)-1, -1, -1):
            second[i] = suffix
            suffix *= nums[i]
        print(second)
        res = []
        for i in range(len(nums)):
            res.append(first[i]*second[i])
        return res
