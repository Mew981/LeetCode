class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        profits = []
        for i in range(len(prices)):
            #find cheapest day
            #do prices[i] - cheapest and append those results to list and return max
            if cheapest > prices[i]:
                cheapest = prices[i]
            profit = prices[i] - cheapest
            profits.append(profit)
        return max(profits)