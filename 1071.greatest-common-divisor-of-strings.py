#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # If no divisors, then addition order should matter
        if str1 + str2 != str2 + str1 :
            return ""

        # If both are divisible perfectly, return any
        if len(str1) == len(str2) :
            return str1

        # Cut the larger string by the smaller string, eventually
        # should hit second base case
        if len(str1) > len(str2) :
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])
    
# @lc code=end

