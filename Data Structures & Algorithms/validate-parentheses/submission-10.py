class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        for char in s:
            if char in char_map.keys():
                stack.append(char)
            elif char in char_map.values():
                if not stack:
                    return False
                if char_map[stack[-1]] != char:
                    return False
                else:
                    stack.pop()
        
        if stack: return False
        
        return True
