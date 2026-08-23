class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        char_set = set()

        if len(s) == 1: return 1
        if len(s) == 0: return 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            
            longest = max(longest, right - left + 1)
        
        return longest