#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        cache = {}

        def dfs(i, j, curr):
           
            if i < 0 or j < 0 or i >= n or j >= m or matrix[i][j] <= curr:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]
            
            curr = matrix[i][j]

            longest = 1 + max(dfs(i + 1, j, curr), dfs(i - 1, j, curr), dfs(i, j + 1, curr), dfs(i, j - 1, curr))

            cache[(i, j)] = longest
            return longest
            
        longestPath = 0
        for i in range(n):
            for j in range(m):
                longestPath = max(longestPath, dfs(i, j, float('-inf')))
            
        return longestPath
        
# @lc code=end

