#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # n = n - 1 + n - 2

        cache = {}

        for i in range(n + 2):
            if i <= 2:
                cache[i] = 1
            else:
                cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n + 1]
    
# @lc code=end

