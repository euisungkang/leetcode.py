#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        net = max_alt = 0

        for i in range(len(gain)) :
            net += gain[i]
            max_alt = max(max_alt, net)
        
        #print(alt)

        return max_alt
    
# @lc code=end

