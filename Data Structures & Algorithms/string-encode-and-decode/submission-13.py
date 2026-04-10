class Solution:
    def encode(self, strs: List[str]) -> str:
        lox = ''
        for i in strs:
            lox += str(len(i)) + '#' + i
        print(lox)
        return lox
    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        size = ''
        while i < len(s):
            if s[i] == '#':
                i+=1
                marley = ''
                for j in range(i, i+int(size)):
                    marley += s[j]
                print(marley)
                l.append(marley)
                i+=int(size)
                size = ''
            else:
                size += s[i]
                i+=1
                print(size)
        return l
        


