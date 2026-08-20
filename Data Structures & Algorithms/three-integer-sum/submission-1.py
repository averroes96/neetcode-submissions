class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        
        for i in range(len(nums)):
            num1 = nums[i]
            rest = {}
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                diff = -num1 - num2
                if diff in rest and [num1, diff, num2] not in output:
                    output.append([num1, diff, num2])
                rest[num2] = j
        
        return output