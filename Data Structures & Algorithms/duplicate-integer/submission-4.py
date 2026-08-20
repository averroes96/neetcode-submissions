class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(set(nums))
        if len(set(nums)) == len(nums):
            return False
        
        return True
        