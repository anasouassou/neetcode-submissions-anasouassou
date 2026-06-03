class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        state = {}
        left = 0
        longestDistinctSize, currentSize = 0, 0

        for right in range(len(s)):

            print('before: ', state)

            state[s[right]] = 1 + state.get(s[right], 0)
            currentSize += 1


            while right - left + 1 > len(state):
                currentSize -= 1
                state[s[left]] -= 1
                if state[s[left]] == 0:
                    del state[s[left]]
                left += 1
            
            print('after: ', state)

            
            longestDistinctSize = max(longestDistinctSize, currentSize)

        return longestDistinctSize