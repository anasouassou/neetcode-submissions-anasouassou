class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        maxSize = 0

        state = {}

        for right in range(len(s)):

            state[s[right]] = 1 + state.get(s[right], 0)

            while right - left + 1 > len(state):
                state[s[left]] -= 1

                if state[s[left]] == 0:
                    del state[s[left]]

                left += 1


            maxSize = max(maxSize, len(state))

        return maxSize