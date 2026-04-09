class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm_alpha = defaultdict(list)
        
        for word in strs:
            hashed_anag = [0]*26
            for letter in word:
                hashed_anag[ord(letter)-ord('a')] += 1
            hm_alpha[''.join(str(hashed_anag))].append(word)
        return list(hm_alpha.values()
        )