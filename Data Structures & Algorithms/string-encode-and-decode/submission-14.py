class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + '#' + word
        print(s)
        return s
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        sizz = ""
        while i < len(s) and s[i] != '#':
            sizz += s[i]
            i += 1
            if s[i] == '#':
                print(sizz)
                strs.append(s[i+1:i+1+int(sizz)])
                i += int(sizz)+1
                sizz = ""
        return strs
        