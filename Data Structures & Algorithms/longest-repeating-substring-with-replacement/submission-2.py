class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency_map = defaultdict(int)
        longest = 0
        left = 0

        if len(s) == 1: return 1

        for right in range(len(s)):
            frequency_map[s[right]] += 1

            while (right - left + 1) - max(frequency_map.values()) > k:
                frequency_map[s[left]] -= 1
                left += 1
            
            longest = max(right - left + 1, longest)
        
        return longest