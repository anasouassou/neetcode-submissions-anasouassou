class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        res = 0
        indexes = {}
        for r in range(len(s)):
            # while s[r] in charSet and l <= r:
            #     charSet.remove(s[l])
            #     l += 1
            # if s[r]
            if s[r] in indexes:
                l = max(indexes[s[r]] + 1, l)
            res = max(r-l+1, res)
            indexes[s[r]] = r
            print(s[r], '####', indexes)


        return res

                


