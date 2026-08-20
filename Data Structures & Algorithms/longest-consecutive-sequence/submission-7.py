class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive_map = defaultdict(int)

        if nums == []: return 0
        counter = 1
        nums = sorted(nums)
        chain = {nums[0]}
        i = 1

        print(nums)

        while i < len(nums):
            if nums[i] == nums[i-1] or nums[i] - 1 == nums[i-1]:
                chain.add(nums[i])
            else:
                counter = max(counter, len(chain))
                chain = {nums[i]}
            
            i += 1

        return max(counter, len(chain))