class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        import math
        mp = defaultdict(int)
        stack = []

        for idx, val in enumerate(position):
            mp[val] = speed[idx]
        
        position = list(reversed(sorted(position)))

        for pos in position:
            will_take = (target - pos) / mp[pos]

            if not stack:
                stack.append((will_take, mp[pos]))
                continue

            if will_take > stack[-1][0]:
                stack.append((will_take, mp[pos]))
                continue
            
            if will_take == stack[-1][0]:
                if mp[pos] == stack[-1][1]:
                    stack.append((will_take, mp[pos]))

        return len(stack)