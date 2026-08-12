class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s={}
        d_t={}
        if len(s) != len(t):
            return False 
        for w in s :
            if w in d_s :
                d_s[w]+=1
            else :
                d_s[w]=1
        for w in t :
            if w in d_t :
                d_t[w]+=1
            else :
                d_t[w]=1
        return (d_s == d_t)
        