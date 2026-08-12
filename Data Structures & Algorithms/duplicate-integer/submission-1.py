class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for ch in nums :
            d[ch] = d.get(ch,0)+1
        for ch in nums :
            if d[ch] >1:
                return True
        return False
