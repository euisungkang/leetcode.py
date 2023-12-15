#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(Counter(arr).values()) == len(set(Counter(arr).values()))
    
# @lc code=end

