class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        res = 0
        for r in range(0, len(s)):
            while s[r] in charSet and l <= r:
                charSet.remove(s[l])
                l += 1
            res = max(r-l+1, res)
            charSet.add(s[r])
        return res

                


