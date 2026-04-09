class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        res = []
        for num in range(len(nums)):
            hm[nums[num]] = hm.get(nums[num], 0) + 1
        print(hm)
        llist = [[] for _ in range(len(nums)+1)]
        for key, value in hm.items():
            llist[value].append(key)
        print(len(llist)-1)
        for i in range(len(llist)-1, -1, -1):
            for j in llist[i]:
                print(j)
                res.append(j)
                if len(res) == k:
                    return res


