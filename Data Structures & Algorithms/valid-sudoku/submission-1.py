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
        sub_box_cache = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] ==".":
                    continue
                initial_length = len(sub_box_cache[(i // 3, j // 3)])
                sub_box_cache[(i//3, j//3)].add(board[i][j]) 
                final_length = len(sub_box_cache[(i // 3, j // 3)])
                
                if final_length == initial_length: 
                    return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.areColumnsValid(board) and self.areRowsValid(board) and self.areSubBoxValid(board) 
        