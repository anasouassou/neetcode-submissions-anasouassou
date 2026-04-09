class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hss, hst = {}, {} 
        for i in range(len(s)):
            hss[s[i]] = hss.get(s[i], 0) + 1
            hst[t[i]] = hst.get(t[i], 0) + 1
        return hss == hst