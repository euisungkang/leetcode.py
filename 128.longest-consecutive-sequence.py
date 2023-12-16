#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : return 0

        hashmap = dict.fromkeys(nums)
        ordered = list(hashmap.keys())
        ordered.sort()

        longest = buffer = 1
        for i in range(len(ordered) - 1) :
            if ordered[i] + 1 == ordered[i + 1] :
                buffer += 1
                if buffer > longest :
                    longest = buffer
            else :
                buffer = 1
            
        return longest
    
# @lc code=end

