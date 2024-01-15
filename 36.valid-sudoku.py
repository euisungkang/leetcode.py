#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # To Track Boxes (3x3)
        boxPerThreeCols = [set() for _ in range(3)]

        # We will traverse cols first by row
        for j in range(9):

            # If we hit a box by row, reset boxes array
            if (j % 3 == 0 and j != 0):
                boxPerThreeCols = [set() for _ in range(3)]

            col = set()
            k = 0
            for i in range(9):

                # If we hit a box by col, add to next box
                if i % 3 == 0 and i != 0:
                    k += 1

                # Col check
                if board[i][j] in col:
                    return False
                
                if board[i][j] != '.':
                    col.add(board[i][j])

                    # Check and add to box
                    if board[i][j] in boxPerThreeCols[k]:
                        return False
                    else:
                        boxPerThreeCols[k].add(board[i][j])

            # Row check
            rowUnique = set(board[j])
            rowUnique.remove('.')
            if len(rowUnique) != len([i for i in board[j] if i != '.']):
                return False

        # Only if col, row, and box check pass
        return True
        
# @lc code=end

