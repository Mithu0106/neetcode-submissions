class Solution:
    def hammingWeight(self, n: int) -> int:
        n=bin(n)
        n=str(n)
        cnt=0
        for i in n :
            if i == "1":
                cnt+=1
        return cnt