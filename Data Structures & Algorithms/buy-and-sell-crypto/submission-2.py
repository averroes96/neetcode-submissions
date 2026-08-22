class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        best = min(prices) - max(prices)

        for right in range(1, len(prices)):
            for left in range(0, right):
                best = max(best, prices[right] - prices[left])
        
        return max(best, 0)