class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        until = [0] * len(temperatures)
        stack = []

        for i, value in enumerate(temperatures):
            while stack and stack[-1][1] < value:
                until[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            
            stack.append((i, value))
        
        return until