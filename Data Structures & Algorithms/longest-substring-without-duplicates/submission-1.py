class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s2=set()
        l=0
        maxx = 0
        for r in range(len(s)):
            while s[r] in s2:
                s2.remove(s[l])
                l+=1
            maxx = max(maxx,r-l+1)
            s2.add(s[r])
        return maxx

