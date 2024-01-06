#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2 : return len(chars)
        
        i = 0            # To Write
        j = [0, 1]       # Sliding Window

        count = 1
        while j[1] <= len(chars):
            if j[1] == len(chars) or chars[j[0]] != chars[j[1]]:
                chars[i] = chars[j[0]]
                if count > 1:
                    countStr = str(count)
                    for digit in countStr:
                        i += 1
                        chars[i] = digit
                
                j[1] += 1
                j[0] += count 
                i += 1
                count = 1

            else:
                j[1] += 1
                count += 1
        
        return len(chars[:i])
        
# @lc code=end

