class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        res=[]
        for n in nums :
            freq[n] = freq.get(n,0)+1
        sortedd = sorted(freq.items(), key = lambda x:x[1] , reverse = True)
        print(sortedd)
        res= [i[0] for i in sortedd[:k]]
        return res
