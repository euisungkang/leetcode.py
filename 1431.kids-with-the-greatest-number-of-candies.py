#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)

        answer = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                answer[i] = True

        return answer
     
# @lc code=end

