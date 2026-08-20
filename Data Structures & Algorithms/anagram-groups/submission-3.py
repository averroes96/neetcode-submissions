class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            count[sorted_word].append(word)
        
        return list(count.values())