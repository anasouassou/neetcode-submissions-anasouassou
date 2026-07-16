class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)

        res = float('inf')


        print(sorted_nums)

        i = 0 
        while i <= len(nums)-k:
            print(sorted_nums[i], sorted_nums[i+k-1])
            res = min(res, sorted_nums[i+k-1] - sorted_nums[i])
            i += 1

        
        return res
