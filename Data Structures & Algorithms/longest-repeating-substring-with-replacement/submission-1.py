class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency_map = defaultdict(int)
        longest = 0
        left = 0

        if len(s) == 1: return 1

        frequency_map[s[left]] += 1

        for right in range(1, len(s)):
            window = s[left:right + 1]
            frequency_map[s[right]] += 1
            window_length = len(window)

            while window_length - max(frequency_map.values()) > k:
                frequency_map[s[left]] -= 1
                left += 1
                window_length -= 1
            
            longest = max(window_length, longest)
        
        return longest