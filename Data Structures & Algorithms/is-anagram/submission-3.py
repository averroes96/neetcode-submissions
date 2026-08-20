class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = {}
        t_table = {}

        for char in s:
            if char in s_table:
                s_table[char] += 1
            else:
                s_table[char] = 1

        for char in t:
            if char in t_table:
                t_table[char] += 1
            else:
                t_table[char] = 1
        
        if len(s_table) != len(t_table):
            return False
        
        for key, value in s_table.items():
            if key not in t_table.keys():
                return False
            if value != t_table[key]:
                return False
        
        return True
        