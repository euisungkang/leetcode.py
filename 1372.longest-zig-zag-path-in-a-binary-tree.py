#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        # dir 0 = left, dir 1 = right
        def dfs(curr, dir, val) :
            if curr is None :
                return val
    
            # left
            if dir == 0 :
                return max(dfs(curr.left, 1, val + 1), dfs(curr.right, 0, 1))
            
            # right
            else :
                return max(dfs(curr.left, 1, 1), dfs(curr.right, 0, val + 1))
        
        return max(dfs(root.right, 0, 1), dfs(root.left, 1, 1)) - 1
    
# @lc code=end

