class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        counter_s1 = {}
        state = {}
        k = len(s1)

        for i in s1:
            counter_s1[i] = 1 + counter_s1.get(i, 0)
        
        for right in range(len(s2)):

            state[s2[right]] = 1 + state.get(s2[right], 0)

            if right - left + 1 > k:
                state[s2[left]] -= 1
                if state[s2[left]] == 0:
                    del state[s2[left]]
                
                left += 1
            
            if state == counter_s1:
                return True
        
        return False
            