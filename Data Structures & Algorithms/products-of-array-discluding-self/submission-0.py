class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffixes = [1] * len(nums)
        prefixes = [1] * len(nums)
        output = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                suffixes[i] *= nums[j]
        
        for i in range(len(nums) - 1, 0, -1):
            for j in range(i-1, -1, -1):
                prefixes[i] *= nums[j]
        
        return [suffixes[i] * prefixes[i] for i in range(len(nums))]