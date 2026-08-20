class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n == 0:
            return 0
        
        lefts = [-1] * n
        rights = [-1] * n

        amount = 0
        max_left = 0
        max_right = n - 1

        lefts[0] = height[0]
        for i in range(1, n):
            lefts[i] = max(lefts[i - 1], height[i])
        
        rights[n-1] = height[n-1]
        for i in range(n - 2, -1, -1):
            rights[i] = max(rights[i + 1], height[i])
        
        for i in range(n):
            amount += min(lefts[i], rights[i]) - height[i]

        return amount