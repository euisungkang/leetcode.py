#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}

        def dfs(i, subt):
            if i >= n:
                return 0
            
            if (i, subt) in cache:
                return cache[(i, subt)]

            cache[(i, subt)] = max(dfs(i + 2, subt) + nums[i], dfs(i + 1, subt))
            return cache[(i, subt)]
        
        return dfs(0, 0)
        
# @lc code=end

