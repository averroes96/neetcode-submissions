class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            h1, h2 = heights[left], heights[right]
            max_area = max(max_area, (right - left) * min(h1, h2))

            if h1 > h2:
                right -= 1
            else:
                left += 1

        return max_area

        