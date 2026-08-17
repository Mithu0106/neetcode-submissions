class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            ss = s[0:i]+s[i+1:]
            if ss == ss[::-1]:
                return True
        return False
