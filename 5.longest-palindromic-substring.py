#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Checks if palindrome : O(n)
        def isPali(s) :
            return s == s[::-1]

        cache = [s[0]]
        longestFound = s[0]

        for i in range(len(s)) :
            buffer = ""
            for j in range(i, len(s)) :

                buffer += s[j]
                if len(buffer) <= len(longestFound) or buffer in cache :
                    continue
                elif isPali(buffer) :
                    #print(i, j, buffer)
                    longestFound = max(longestFound, buffer, key=len)
                    cache.append(buffer)

        return longestFound

        # Brute Force

        # def isPali(s) :
        #     return s == s[::-1]

        # longestFound = ""

        # for i in range(len(s)) :
        #     buffer = ""
        #     for j in range(i, len(s)) :

        #         buffer += s[j]
        #         if isPali(buffer) :
        #             #print(i, j, buffer)
        #             longestFound = max(longestFound, buffer, key=len)

        # return longestFound
    
# @lc code=end

