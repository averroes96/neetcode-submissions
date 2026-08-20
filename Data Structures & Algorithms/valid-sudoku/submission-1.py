class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        square_map = defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if val == ".": continue
                if val in row_map[row]: return False
                if val in col_map[col]: return False
                if val in square_map[(row // 3, col // 3)]: return False

                row_map[row].add(val)
                col_map[col].add(val)
                square_map[(row // 3, col // 3)].add(val)

        return True