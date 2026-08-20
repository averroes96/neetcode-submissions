class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        
        for i in range(len(nums)):
            num1 = nums[i]
            
            if num1 > 0: break

            if i > 0 and num1 == nums[i - 1]:
                continue

            rest = {}
            left, right = i + 1, len(nums) - 1
            while left < right:
                num2 = nums[left]
                num3 = nums[right]
                target = num1 + num2 + num3
                if target > 0:
                    right -= 1
                elif target < 0:
                    left += 1
                else:
                    output.append([num1, num2, num3])
                    left += 1
                    right -= 1
                    
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                
            # for j in range(i + 1, len(nums)):
            #     num2 = nums[j]
            #     diff = -num1 - num2
            #     if diff in rest and [num1, diff, num2] not in output:
            #         output.append([num1, diff, num2])
            #     rest[num2] = j
        
        return output