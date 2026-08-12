class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        res=[]
        for ch in nums:
            freq[ch] = freq.get(ch,0)+1
        sortedd = sorted(freq.items() , key = lambda x:x[1] , reverse = True)
        res=(d[0] for d in sortedd[:k])
        return list(res)

