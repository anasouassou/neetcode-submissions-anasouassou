class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums)):
            
            if i > 0 and nums[i-1] == nums[i]:
                continue

            left, right = i + 1, len(nums)-1

            while left < right:
                # print(nums)
                # print(i, left, right)
                # print(nums[i] + nums[left] + nums[right])
                # print('####')

                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
        
                else:
                    left += 1
                
            
        return result