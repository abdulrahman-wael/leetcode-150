# thanks to Allah, I did solve this problem by myself then discovered that my solution was actually dynamic programming
# this solution is a variation of Kadane's algorithm.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        base = prices[0]
        for price in prices:
            if price < base:
                base = price
            elif price - base > profit:
                profit = price - base
        return profit