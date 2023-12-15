#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#

# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list1 = set(nums1) - set(nums2)
        list2 = set(nums2) - set(nums1)
        return [list1, list2]
    
# @lc code=end

