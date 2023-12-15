#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        order = deque([root])
        curr_node = root
        max_sum = [1, root.val]     #Initialize max_sum to [root lvl, root val]

        level = 0
        while order :
            level += 1
            level_sum = 0

            for i in range(len(order)) :
                curr_node = order.popleft()
                level_sum += curr_node.val

                if curr_node.left is not None :
                    order.append(curr_node.left)
                if curr_node.right is not None :
                    order.append(curr_node.right)
            
            # If current level sum greater than max so far, update
            if level_sum > max_sum[1] :
                max_sum = [level, level_sum]

        return max_sum[0]
         
# @lc code=end

