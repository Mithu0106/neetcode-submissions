class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        res=[]
        for n in nums :
            freq[n] = freq.get(n,0)+1
        sortedd = sorted(freq.items() , key = lambda x:x[1] ,reverse = True)
        res= [item[0] for item in sortedd[:k]]
        return res


