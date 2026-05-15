class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        frequency = {}
        maxf = 0
        res = 0
        for r in range(len(s)):

            frequency[s[r]] = 1 + frequency.get(s[r], 0)
            maxf = max(maxf, frequency[s[r]])

            while r-l+1 - maxf > k:
                frequency[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)

        return res