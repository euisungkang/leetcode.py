#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        sa = list(s)

        vowels = ['a','A','e','E','i','I','o','O','u','U']

        while i < j:
            if sa[i] not in vowels:
                i += 1
            if sa[j] not in vowels:
                j -= 1
            
            if sa[i] in vowels and sa[j] in vowels:
                sa[i], sa[j] = sa[j], sa[i]
                i += 1
                j -= 1
            
        return ''.join(sa)
        
# @lc code=end

