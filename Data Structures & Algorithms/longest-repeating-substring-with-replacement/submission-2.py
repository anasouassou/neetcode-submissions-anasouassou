class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        maxSize = 0
        res = 0
        state = {}

        for right in range(len(s)):
            
            state[s[right]] = 1 + state.get(s[right], 0)
            maxSize = max(maxSize, state[s[right]])

            while right - left + 1 - maxSize > k:
                state[s[left]] -= 1
                if state[s[left]] == 0:
                    del state[s[left]]
                left += 1

            res = max(res, right-left+1)

        return res