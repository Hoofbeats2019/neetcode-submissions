class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we can use the prefix and suffix algrithem 
        prefix = []
        suffix = []

        current = prices[0]
        for price in prices:
            current = min(price, current)
            prefix.append(current)
        
        current = prices[-1]
        for price in reversed(prices):
            current = max(price, current)
            suffix.append(current)
        suffix.reverse()

        profits = [suf - pre for suf, pre in zip(suffix, prefix)]
        return max(profits)

