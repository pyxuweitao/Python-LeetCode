__author__ = 'xuweitao'
#runtime = 64ms
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        profit = 0
        if len( prices ) != 0:
            min_price = prices[0]
            for iPrice in prices:
                if iPrice < min_price:
                    min_price = iPrice
                profit = iPrice - min_price if iPrice - min_price > profit else profit

        return profit