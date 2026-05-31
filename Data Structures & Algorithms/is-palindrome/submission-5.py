class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not self.isalpha(s[left]):
                left += 1
            while left < right and not self.isalpha(s[right]):
                right -= 1
            # print(s[left], ' ', s[right])
            if s[right].lower() != s[left].lower():
                return False
            left += 1
            right -= 1
        
        return True
    
    def isalpha(self, c):
        return (ord('a') <= ord(c) <= ord('z')) or \
        (ord('A') <= ord(c) <= ord('Z')) or \
        (ord('0') <= ord(c) <= ord('9'))