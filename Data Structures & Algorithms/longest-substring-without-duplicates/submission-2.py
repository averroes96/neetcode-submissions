class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0

        if len(s) == 1: return 1
        if len(s) == 0: return 0

        for right in range(1, len(s)):
            while s[right] in s[left:right] and left < right:
                left += 1
            
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest