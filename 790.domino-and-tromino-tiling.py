#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        
        cache = []  # i : total dominoes at size 2 * i

        D, T = {1 : 1, 2 : 2}, {1 : 0, 2 : 1}
        
        # https://leetcode.com/problems/domino-and-tromino-tiling/description/?envType=study-plan-v2&envId=leetcode-75
        for i in range(3, n + 1) :
            D[i] = D[i - 1] + D[i - 2] + T[i - 1] * 2
            T[i] = T[i - 1] + D[i - 2]
        
        return D[n] % (10 ** 9 + 7)
        
# @lc code=end

