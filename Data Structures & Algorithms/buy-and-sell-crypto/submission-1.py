class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        low = 0

        profit = 0
        for i in range(1,len(prices)):
            low  = i-1 if prices[i-1] < prices[low] else low
            profit = max(profit, prices[i]-prices[low])

        return max(profit, prices[i]-prices[low])