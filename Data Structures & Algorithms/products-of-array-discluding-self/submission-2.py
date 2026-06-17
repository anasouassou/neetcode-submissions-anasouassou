class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftArray, rightArray = ([1 for _ in range(len(nums))], [1 for _ in range(len(nums))])
        res = []
        helper = 1

        for i in range(1, len(nums)):
            helper *= nums[i-1]
            leftArray[i] = helper
            print(helper)

        print(leftArray)

        helper = 1

        for i in range(len(nums)-2, -1, -1):
            helper *= nums[i+1]
            rightArray[i] = helper
            print(helper)
        
        print(rightArray)

        for i in range(len(nums)):
            res.append(leftArray[i]*rightArray[i])
        
        return res


            