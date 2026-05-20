class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        freq_inverse = {}
        res = []
        buckets = [[] for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
        # print(freq)
        for number, count in freq.items():
            buckets[count].append(number)
        # print(bucket)
        to_break = 0
        for i in range(len(nums), 0, -1):
            current_bucket = buckets[i]
            print(current_bucket)
            for j in current_bucket:
                if to_break == k:
                    break
                res.append(j)
                to_break += 1
        return res



