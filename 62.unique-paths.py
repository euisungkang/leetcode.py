#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = {}   #(x, y) : num of unique paths

        def dfs(i, j) :

            if i >= m - 1 or j >= n - 1 :
                return 1

            if (i, j) in cache :
                #print('cached', cache[(i,j)])
                return cache[(i, j)]

            cache[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
            #print(i ,j, cache[(i,j)])
            return cache[(i, j)]

        return dfs(0, 0)
    
# @lc code=end

