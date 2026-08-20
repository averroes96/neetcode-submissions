class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency = defaultdict(int)
        # most_freq = []
        # i = 0

        # for num in nums:
        #     frequency[num] += 1
        
        # def sorting_key(num):
        #     return frequency[num]
        
        # nums = sorted(nums, key=sorting_key, reverse=True)

        # for num in nums:
        #     if num not in most_freq:
        #         most_freq.append(num)
        #         i += 1
            
        #     if i == k:
        #         return most_freq
        
        # return most_freq

        occurrences = [[] for i in range(len(nums) + 1)]
        freq = defaultdict(int)
        out = []

        for num in nums:
            freq[num] += 1
        
        for key, val in freq.items():
            occurrences[val].append(key)
        
        for i in range(len(occurrences) - 1, 0, -1):
            for num in occurrences[i]:
                out.append(num)
                if len(out) == k:
                    return out



        