class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1
        

        while left < right:
            val1 = numbers[left]
            val2 = numbers[right]

            if val1 + val2 == target:
                return [left + 1, right + 1]
            elif val1 + val2 > target:
                right -= 1
            else:
                left += 1
        
        return [left, right]