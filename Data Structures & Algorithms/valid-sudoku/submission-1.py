class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rule 1 - each row must contain the digits 1-9 without duplicates
        for row in board:
            row_map = {}
            for square in row:
                if square == ".":
                    continue
                
                if square not in row_map:
                    row_map[square] = 1
                else:
                    row_map[square] = row_map[square] + 1
                    return False
        
        # Check rule 2 - each column must contain the digits 1-9 without duplicates
        for column in zip(*board):
            column_map = {}
            for square in column:
                if square == ".":
                    continue

                if square not in column_map:
                    column_map[square] = 1
                else:
                    column_map[square] = column_map[square] + 1
                    return False
        
        # Check rule 3 - each sub-board contain digits 1-9 without duplication
        sub_board_map = {}
        for row in range(9):
            for column in range(9):
                # find the subboard index for board[row][column]
                index = (row // 3) * 3 + (column // 3)
                square = board[row][column]
                if square == ".":
                    continue
                
                if index not in sub_board_map:
                    sub_board_map[index] = {}
                
                
                if square not in sub_board_map[index]:
                    sub_board_map[index][square] = 1
                else:
                    sub_board_map[index][square] = sub_board_map[index][square] + 1
                    return False
        return True
        