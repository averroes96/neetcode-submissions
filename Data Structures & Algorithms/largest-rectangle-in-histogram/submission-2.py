class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for index, value in enumerate(heights):
            start = index

            while stack and stack[-1][1] > value:
                prev_index, prev_value = stack.pop()
                max_area = max(max_area, prev_value * (index - prev_index))
                start = prev_index
            
            stack.append((start, value))
        
        for index, value in stack:
            max_area = max(max_area, value * (len(heights) - index))

        return max_area

            
            