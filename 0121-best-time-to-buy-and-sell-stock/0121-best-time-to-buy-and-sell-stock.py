class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        max_profit = 0
        #
        while right < len(prices) :
            if prices[left] < prices[right]:
                if max_profit < prices[right] - prices[left]:
                    max_profit = prices[right] - prices[left]
                    right = right + 1
                else:
                    right = right + 1    
            elif prices[left] >= prices[right]:
                left = right
                right = right + 1
        return max_profit