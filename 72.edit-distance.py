#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        cache = {}   # (i, j) : min(operations)

        def dfs(i, j) :

            # Base Cases where string is out of bounds
            # Default is word - index : # of inserts from ""
            if i >= len(word1) :
                return len(word2) - j
            if j >= len(word2) :
                return len(word1) - i

            # If match, move to next char in both strings (no op cost)
            if word1[i] == word2[j] :
                return dfs(i + 1, j + 1)

            # Search cache
            if (i, j) in cache :
                return cache[(i, j)]
        
            # Considers insert, delete, and replace
            minOps = 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1))

            cache[(i, j)] = minOps
            return minOps

        return dfs(0, 0)

# @lc code=end
        