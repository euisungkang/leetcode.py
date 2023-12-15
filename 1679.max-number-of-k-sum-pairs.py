#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()

        def scan(i, j, ans) :
            if i >= j :
                return ans
            elif nums[i] + nums[j] == k :
                return scan(i + 1, j - 1, ans + 1)
            elif nums[i] + nums[j] < k :
                return scan(i + 1, j, ans)
            else :
                return scan(i, j - 1, ans)

        return scan(0, len(nums) - 1, 0)
    
# @lc code=end

