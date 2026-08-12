class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        d_s={}
        d_t={}
        for i in range(len(s)):
            d_s[s[i]] = d_s.get(s[i],0)+1
            d_t[t[i]] = d_t.get(t[i],0)+1
        # for w in s :
        #     if w in d_s :
        #         d_s[w]+=1
        #     else :
        #         d_s[w]=1
        # for w in t :
        #     if w in d_t :
        #         d_t[w]+=1
        #     else :
        #         d_t[w]=1
        return d_s == d_t
        