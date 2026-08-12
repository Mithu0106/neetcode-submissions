class Solution:
    def countBits(self, n: int) -> List[int]:
        ans =[]
        for i in range(n+1):
            bi = bin(i)
            countt = bi.count("1")
            ans.append(countt)
        return ans

