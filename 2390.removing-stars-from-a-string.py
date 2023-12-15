#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
class Solution:

    #My Original Implementation.  Mistake: Instead of traversing the original s, and 
    # incrementally adding to a stack. I initialized the stack as s. Not fully using
    # the perks of stacks.. rather I overcomplicated it by using useless loops and
    # counts for # of '*'...
    # def removeStars(self, s: str) -> str:
    #     stack = deque(s)
    #     ans = ""
    #     pop_count = 0

    #     while stack :
    #         buffer = stack.pop()

    #         if buffer == '*' :
    #             pop_count += 1
    #         elif pop_count > 0 and buffer != '*' :
    #             pop_count -= 1
    #         else :
    #             ans = buffer + ans

    #     return ans

    # Iterate over s and use right adding and popping utility of stacks to add and
    # remove when '*'
    def removeStars(self, s: str) -> str:
        ans = deque()

        for i in range(len(s)) :
            if s[i] == '*' :
                ans.pop()
            else :
                ans.append(s[i])

        return ''.join(ans)

# @lc code=end

