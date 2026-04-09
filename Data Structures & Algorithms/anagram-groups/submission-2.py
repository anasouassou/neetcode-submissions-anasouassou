class Solution:
    def createCharFrequency(self, word: str) -> tuple:
        freq_list = [0] * 26
        for char in word:
            freq_list[ord(char) - ord('a')] += 1
        return tuple(freq_list)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            freq_tuple = self.createCharFrequency(word)
            groups[freq_tuple].append(word)
        return list(groups.values())
            
