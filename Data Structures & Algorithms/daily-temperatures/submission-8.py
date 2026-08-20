class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        # for i in range(len(temperatures) - 1):
        #     j = i + 1
        #     while j < len(temperatures):
        #         if temperatures[j] > temperatures[i]:
        #             result[i] = j - i
        #             break
                
        #         j += 1

        for i, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            
            stack.append(i)
                
        return result