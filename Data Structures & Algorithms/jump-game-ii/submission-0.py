class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0 
        r = 0
        res = 0

        while r < len(nums)-1:
            maxMfJump = 0
            print("l: ", l, "r: ", r)
            for i in range(l, r + 1) :
                maxMfJump = max(maxMfJump, i+nums[i])
                print('maxMfJump', maxMfJump)
            l = r + 1
            r = maxMfJump
            res += 1
            print('res: ', res, '\n#######################')

        return res
        