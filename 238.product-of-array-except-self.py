#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        prefixSum = 1
        suffixSum = 1

        for i in range(len(nums)):
            answer[i] = answer[i] * prefixSum
            prefixSum *= nums[i]

        for j in range(len(nums) - 1, -1, -1):
            answer[j] = answer[j] * suffixSum
            suffixSum *= nums[j]

        return answer
        
# @lc code=end

