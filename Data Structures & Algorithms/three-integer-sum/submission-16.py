class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            
            if i > 0 and nums[i-1] == nums[i]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:

                if nums[left] + nums[right] + nums[i] == 0:
                    res.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while left > 0 and nums[left] == nums[left-1] and left < len(nums)-1:
                        left += 1
                
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                    
                
                else: 
                    left += 1
                    


        return res