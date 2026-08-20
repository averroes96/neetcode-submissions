class Solution:
    def trap(self, height: List[int]) -> int:
        lefts = [-1] * len(height)
        rights = [-1] * len(height)

        amount = 0

        max_left = 0
        max_right = len(height) - 1

        for i in range(1, len(height)):
            h = height[i]
            if h >= height[max_left]:
                max_left = i
            else:
                lefts[i] = max_left
        
        for i in range(len(height) - 1, -1, -1):
            h = height[i]
            if h >= height[max_right]:
                max_right = i
            else:
                rights[i] = max_right
        
        for i in range(len(height)):
            left, right = lefts[i], rights[i]

            if left == -1 or right == -1:
                continue
            
            amount += min(height[left], height[right]) - height[i]

        return amount