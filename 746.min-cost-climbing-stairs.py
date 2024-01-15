#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = {n : 0}

        # 1 or 2 steps
        # Start at either i = 0 or i = 1
        def dfs(i):
            if i > n:
                return float('inf')

            if i in cache:
                return cache[i]
            
            cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return cache[i]
            
        return min(dfs(0), dfs(1))
    
# @lc code=end

