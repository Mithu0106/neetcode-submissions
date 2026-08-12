class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        n=len(nums)
        need = n/2
        for n in nums :
            d[n]=d.get(n,0)+1
            if d[n] >= need :
                return n
        