class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxProfit = 0
        buy, sell = 0, 1
        for i in range(len(prices)):
            if len(prices) == sell:
                break
            profit = prices[sell] - prices[buy]
            if profit > MaxProfit:
                MaxProfit = profit
            if prices[sell] < prices[buy]:
                buy = sell
                sell = buy + 1
            else:
                 sell += 1
        return MaxProfit
