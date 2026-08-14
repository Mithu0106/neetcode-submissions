class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=set()
        maxx = 0
        l=0
        for r in range(len(s)):
            while s[r] in d :
                d.remove(s[l])
                l+=1
            maxx = max(maxx,r-l+1)
            d.add(s[r])
        return maxx

