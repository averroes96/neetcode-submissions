class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        fresh_count = 0
        minutes = 0
        queue = deque()

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    fresh_count += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))
        
        if fresh_count == 0:
            return 0

        def _neighbors(position):
            row, col = position
            neighbors = (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)
            return neighbors
        
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                current = queue.popleft()
                row, col = current
                neighbors = _neighbors(current)

                for neighbor in neighbors:
                    d_row, d_col = neighbor

                    if 0 <= d_row < n and 0 <= d_col < m and grid[d_row][d_col] == 1:
                        grid[d_row][d_col] = 2
                        fresh_count -= 1
                        queue.append(neighbor)
            
            minutes += 1
        
        return minutes if fresh_count == 0 else -1
