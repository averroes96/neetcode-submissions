class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        islands = 0

        def _neighbors(pos):
            row, col = pos
            return (row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)

        def DFS(position):
            row, col = position
            value = grid[row][col]

            if value == "0":
                return
            
            grid[row][col] = "0"
            neighbors = _neighbors(position)

            for neighbor in neighbors:
                row, col = neighbor
                if (row == n or col == m or row < 0 or col < 0):
                    continue
                
                DFS(neighbor)
        
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1":
                    islands += 1
                DFS((row, col)) 

        return islands