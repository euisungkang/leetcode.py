#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        longest = max(len(word1), len(word2))
        for i in range(longest):
            if i >= len(word1) :
                merged += word2[i:len(word2)]
                return merged
            elif i >= len(word2) :
                merged += word1[i:len(word1)]
                return merged
            
            merged += word1[i] + word2[i]

        return merged
    
# @lc code=end

