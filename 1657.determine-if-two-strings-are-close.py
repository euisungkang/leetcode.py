#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        operation_1 = len(word1) == len(word2)
        operation_2 = set(word1) == set(word2)
        operation_3 = Counter(Counter(word1).values()) == Counter(Counter(word2).values())

        return operation_1 and operation_2 and operation_3
        
# @lc code=end

