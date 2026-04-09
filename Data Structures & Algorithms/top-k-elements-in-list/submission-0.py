class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        buckets = [[] for _ in range(len(nums)+1)]

        for i in nums:
            count_dict[i] = 1 + count_dict.get(i, 0)
        
        for key, count in count_dict.items():
            buckets[count].append(key)

        res = []

        for i in range(len(buckets)-1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res