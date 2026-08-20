class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for word in strs:
            matrice = [0] * 26
            for letter in word:
                pos = ord(letter) - ord("a")
                matrice[pos] += 1
            
            matrice = tuple(matrice)
            
            count[matrice].append(word)

        return list(count.values())