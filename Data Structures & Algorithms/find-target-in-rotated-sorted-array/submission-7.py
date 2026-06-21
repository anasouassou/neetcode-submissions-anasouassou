class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            
            middle = left + (right - left)//2

            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
            
        pivot = left
            
        left, right = 0, len(nums) - 1

        if nums[pivot] <= target <= nums[right]:
            left = pivot
        else:
            right = pivot-1

        while left <= right:

            middle = left + (right - left)//2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
            
        return -1