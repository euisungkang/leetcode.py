#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        # Use single pass map initialization : O(1)

        map = {}
        for i in range(len(nums)) :
            complement = target - nums[i]

            # Initialized key = nums[i], val = i
            if (complement in map) :
                return[map[complement], i]
            map[nums[i]] = i
        
        return []
        
# @lc code=end

