#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = Counter(s)
        t_map = Counter(t)

        if s_map == t_map:
            return True
        return False
        
# @lc code=end

