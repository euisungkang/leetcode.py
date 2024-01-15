#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        cache = {}

        # answer = [0]
        def dfs(i, subt):
            if subt > amount or i >= n:
                return 0
            if subt == amount:
                return 1
            
            if (i, subt) in cache:
                return cache[(i, subt)]

            cache[(i, subt)] = dfs(i, subt + coins[i]) + dfs(i + 1, subt)
            return cache[(i, subt)]
        
        return dfs(0, 0)
        
# @lc code=end

