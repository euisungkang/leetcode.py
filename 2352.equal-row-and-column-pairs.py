#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = 0

        dim = len(grid)

        cols = []
        for i in range(dim) :
            col = []
            for j in range(dim) :
                col.append(grid[j][i])
            cols.append(col)
        
        #print(cols)

        for i in range(dim) :
            for j in range(dim) :
                if grid[i] == cols[j] :
                    pairs += 1

        return pairs
    
# @lc code=end

