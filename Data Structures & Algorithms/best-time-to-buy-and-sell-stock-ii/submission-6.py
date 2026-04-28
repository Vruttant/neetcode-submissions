class Solution:
    def rec(self, i, bought, prices, cache):
        import sys
        sys.setrecursionlimit(2000)
        if i == len(prices):
            return 0 

        if (i, bought) in cache:
            return cache[(i, bought)]

        res = self.rec(i + 1, bought, prices, cache)

        if bought: 
            res = max(res, prices[i] + self.rec(i + 1, False, prices, cache))
        else:
            res = max(res, -prices[i] + self.rec(i + 1, True, prices, cache))
        
        cache[(i, bought)] = res 

        return res 
        
    def maxProfit(self, prices: List[int]) -> int:
        return self.rec(0, False, prices, {})