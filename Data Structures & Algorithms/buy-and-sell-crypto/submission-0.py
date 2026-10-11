class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min , max = prices[0] , prices[0]
        profit = 0 
        for i in range(1, len(prices)):
            if prices[i] < min and (i != len(prices) - 1 ):
                min = prices[i]
                max = 0 
            if prices[i] > max:
                max = prices[i]
            temp = max - min
            if  temp > profit:
                profit = temp 
        return profit           