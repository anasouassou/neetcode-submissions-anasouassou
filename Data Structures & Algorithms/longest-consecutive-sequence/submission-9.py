class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        hs = set(nums)
        res = 1
        for i in range(len(nums)):
            j = 1
            temp = 1
            if nums[i]-1 not in hs:
                print('processing ', nums[i], ':')
                while nums[i]+j in hs:
                    print('\t found ', nums[i]+j)
                    j+=1
                    temp+=1
                res = max(temp, res)
                print('\t res now = ', res)
            else:
                print('value :', nums[i], 'minus 1 already exists')
        return res