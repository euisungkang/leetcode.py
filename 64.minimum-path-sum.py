#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cache = { (m - 1, n - 1) : grid[-1][-1] }

        def djikstra(i, j) :
            if (i, j) in cache :
                return cache[(i, j)]
            if i >= m or j >= n :
                return float('inf')
        
            shortest = min(djikstra(i + 1, j), djikstra(i, j + 1))

            cache[(i, j)] = grid[i][j] + shortest

            return cache[(i, j)]

        return djikstra(0, 0)
        
# @lc code=end

