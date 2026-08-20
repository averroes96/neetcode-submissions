class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for index, value in enumerate(heights):
            start = index
            while stack and stack[-1][1] > value:
                prev_index, prev_value = stack.pop()
                start = prev_index
                area = prev_value * (index - prev_index)
                max_area = max(max_area, prev_value * (index - prev_index))
            
            stack.append((start, value))
        
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))

        return max_area

            
            