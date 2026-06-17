class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + (right-left)//2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        pivot = left

        left, right =  0, len(nums) - 1

        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else: 
            right = pivot - 1

        while left <= right:
            middle = left + (right-left)//2

            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else: 
                right = middle - 1
        
        return -1
        



