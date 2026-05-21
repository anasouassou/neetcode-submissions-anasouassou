class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            while left < right and not self.isascii(s[left]):
                left += 1
            while left < right and not self.isascii(s[right]):
                right -= 1
            print(left, ' ', right)
            if s[left].lower() != s[right].lower() :
                return False
            left, right = left + 1, right - 1
        return True

    def isascii(self, c):
        return (
            (ord('a') <= ord(c) <= ord('z'))
        ) or (
            (ord('A') <= ord(c) <= ord('Z'))
        ) or (
            (ord('0') <= ord(c) <= ord('9'))
        )
