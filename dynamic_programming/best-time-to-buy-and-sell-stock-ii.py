class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        base = prices[0]
        profit = 0
        for price in prices:
            if price > base:
                profit += (price - base)
            base = price
        return profit

        # # another more optimized solution:
        # profit = 0

        # # Every upward step can be taken as a separate transaction.
        # # Adding all positive day-to-day gains equals the optimal total profit.
        # for i in range(1, len(prices)):
        #     if prices[i] > prices[i - 1]:
        #         profit += prices[i] - prices[i - 1]

        # return profit
