#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = {}

        def dfs(i, bought):
            if i >= n:
                return 0

            if (i, bought) in cache:
                return cache[(i, bought)]
            
            if not bought:
                # Buy
                maxProfit = max(dfs(i + 1, True) - prices[i], dfs(i + 1, bought))

            else:
                # Sell
                maxProfit = max(dfs(i + 2, False) + prices[i], dfs(i + 1, bought))

            cache[(i, bought)] = maxProfit
            return cache[(i, bought)]

        return dfs(0, False)
        
# @lc code=end

