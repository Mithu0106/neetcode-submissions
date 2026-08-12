class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxx = 0
        for i in range(n):
            for j in range(i+1,n):
                pro = prices[j] - prices[i]
                if pro > maxx :
                    maxx=pro
        return maxx