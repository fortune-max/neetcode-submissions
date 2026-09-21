class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price, ans = -float("inf"), 0
        for price in reversed(prices):
            ans = max(ans, max_price - price)
            max_price = max(max_price, price)
        return ans
