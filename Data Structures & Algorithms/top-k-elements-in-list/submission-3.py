class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        most_freq = []
        i = 0

        for num in nums:
            frequency[num] += 1
        
        def sorting_key(num):
            return frequency[num]
        
        nums = sorted(nums, key=sorting_key, reverse=True)

        for num in nums:
            if num not in most_freq:
                most_freq.append(num)
                i += 1
            
            if i == k:
                return most_freq
        
        return most_freq