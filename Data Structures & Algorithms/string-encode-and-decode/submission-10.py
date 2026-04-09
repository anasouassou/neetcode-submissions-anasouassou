class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs: 
            return ""

        res = ""
        for word in strs:
            res += str(len(word)) + ',' + word

        res += '#'
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i = 0
        print(s)
        res = []
        while s[i] != '#':
            size, temp = "", ""
            while s[i] != ',':
                size += s[i]
                i += 1
            size = int(size)
            i += 1
            for j in range(i, i+size):
                temp += s[j]
            i += size
            res.append(temp)
        return res

        
        
# class Solution:
#     def encode(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         res = ""
#         for word in strs:
#             res += str(len(word)) + ',' + word
#         res += '#'  # End marker
#         return res

#     def decode(self, s: str) -> List[str]:
#         if not s:
#             return []
#         i = 0
#         res = []  # Initialize result list once before loop
#         while s[i] != '#':
#             size = ""
#             while s[i] != ',':
#                 size += s[i]
#                 i += 1
#             size = int(size)
#             i += 1  # skip comma
#             temp = s[i:i+size]
#             res.append(temp)
#             i += size  # Move i forward by size
#         return res


        
