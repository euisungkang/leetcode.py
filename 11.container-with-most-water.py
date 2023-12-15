#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        max_volume = min(height[left], height[right]) * (len(height) - 1)

        while (left < right) :
            if height[left] <= height[right] :
                minimum_volume = height[left]
                left += 1
            elif height[left] > height[right] :
                minimum_volume = height[right]
                right -= 1

            volume = minimum_volume * (right - left + 1)
            if max_volume < volume :
                max_volume = volume

        return max_volume
        
# @lc code=end