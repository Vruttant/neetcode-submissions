from collections import defaultdict
class Solution:
    def areRowsValid(self, board):
        rows_cache = defaultdict(set)

        for row_idx in range(9):
            for col_idx in range(9):
                initial_length = len(rows_cache.get(row_idx, {}))
                cell_value = board[row_idx][col_idx]
                if cell_value != ".":
                    rows_cache[row_idx].add(cell_value)
                    final_length = len(rows_cache.get(row_idx))

                    if initial_length == final_length:
                        return False 
        return True

    def areColumnsValid(self, board):
        col_cache = defaultdict(set)

        for col_idx in range(9):
            for row_idx in range(9):
                initial_length = len(col_cache.get(col_idx, {}))
                cell_value = board[row_idx][col_idx]
                if cell_value != ".":
                    col_cache[col_idx].add(cell_value)
                    final_length = len(col_cache.get(col_idx))
                
                    if initial_length == final_length:
                        return False 
        print(col_cache)
        return True
    
    def areSubBoxValid(self, board):
        seen = defaultdict(set)
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True



    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.areColumnsValid(board) and self.areRowsValid(board) and self.areSubBoxValid(board) 
        