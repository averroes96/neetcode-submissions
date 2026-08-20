class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        
        for i in range(len(nums)):
            num1 = nums[i]
            rest = {}
            left, right = i + 1, len(nums) - 1
            while left < right:
                target = -num1
                num2 = nums[left]
                num3 = nums[right]
                if num2 + num3 > target:
                    right -= 1
                elif num2 + num3 < target:
                    left += 1
                else:
                    if [num1, num2, num3] not in output:
                        output.append([num1, num2, num3])
                    left += 1
                    right -= 1
                
            # for j in range(i + 1, len(nums)):
            #     num2 = nums[j]
            #     diff = -num1 - num2
            #     if diff in rest and [num1, diff, num2] not in output:
            #         output.append([num1, diff, num2])
            #     rest[num2] = j
        
        return output