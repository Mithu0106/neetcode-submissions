class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s={}
        d_t={}
        if len(s) != len(t):
            return False 
        for w in s:
            d_s[w] = d_s.get(w,0)+1
        for w in t :
            d_t[w] = d_t.get(w,0)+1
        return d_s == d_t