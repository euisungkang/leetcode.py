#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = heapq.nlargest(k, nums)

        return heap[-1]
        
# @lc code=end

