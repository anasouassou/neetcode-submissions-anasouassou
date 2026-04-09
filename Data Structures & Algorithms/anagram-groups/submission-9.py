class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for stri in strs:
            sortedStr = ''.join(sorted(stri))
            hm[sortedStr].append(stri)
        return list(hm.values())