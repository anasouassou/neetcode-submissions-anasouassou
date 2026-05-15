class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        freq_s1 = {}
        current_freq_s2 = {}
        for i in range(len(s1)):
            freq_s1[s1[i]] = 1 + freq_s1.get(s1[i], 0)
        
        for r in range(0, len(s2)):
            current_freq_s2[s2[r]] = 1 + current_freq_s2.get(s2[r], 0)

            if (r-l)+1 > len(s1):
                current_freq_s2[s2[l]] -= 1
                if current_freq_s2[s2[l]] == 0:
                    del current_freq_s2[s2[l]]
                l += 1
            
            if current_freq_s2 == freq_s1:
                return True
        return False