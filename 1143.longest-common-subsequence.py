#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cache = {}   # (i, j) : max length of substring

        def dfs(i, j) :
            if i >= len(text1) or j >= len(text2) :
                return 0
            if text1[i] == text2[j] :
                return 1 + dfs(i + 1, j + 1)
            if (i, j) in cache :
                return cache[(i, j)]
            
            cache[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return cache[(i, j)]

        return dfs(0, 0)
    
# @lc code=end

