class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}
        for i in range(len(nums)):
            for key, value in needed.items():
                if value == nums[i]:
                    return [key, i]
            needed[i] = target - nums[i]
        
        return [0, 1]

