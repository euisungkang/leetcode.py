#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in cache:
                cache[sorted_s].append(s)
            else:
                cache[sorted_s] = [s]

        return cache.values()

        
# @lc code=end

