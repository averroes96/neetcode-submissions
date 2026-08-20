class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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



        