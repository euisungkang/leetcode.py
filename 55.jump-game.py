#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        cache = { len(nums) - 1 : True }

        def dfs(i) :
            if i >= len(nums) :
                return False
            
            if i in cache :
                #print("Triggered")
                return cache[i]

            for j in range(i + nums[i], i, -1) :
                #print(i, j)
                if dfs(j) :
                    cache[i] = True
                    return True

            cache[i] = False
            return False

        return dfs(0)
            
        
# @lc code=end

