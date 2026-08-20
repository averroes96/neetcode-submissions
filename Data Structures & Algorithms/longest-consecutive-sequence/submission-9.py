class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: 
            return 0
        counter = 1
        nums = list(sorted(set(nums)))
        chain = [nums[0]]
        i = 1

        while i < len(nums):
            if nums[i] - 1 == nums[i-1]:
                chain.append(nums[i])
            else:
                counter = max(counter, len(chain))
                chain = [nums[i]]
            
            i += 1

        return max(counter, len(chain))