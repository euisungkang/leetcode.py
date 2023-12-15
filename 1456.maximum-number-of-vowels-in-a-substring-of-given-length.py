#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
from collections import Counter

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        initial = Counter(s[:k])
        maxVowel = sum([initial[v] for v in vowels])

        count = maxVowel
        for i in range(len(s) - k) :
            if s[i] in vowels and s[i + k] not in vowels :
                count -= 1
            elif s[i] not in vowels and s[i + k] in vowels :
                count += 1
                if count > 0 :
                    maxVowel = max(maxVowel, count)

        return maxVowel
        
# @lc code=end

