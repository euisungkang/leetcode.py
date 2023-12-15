#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Edge Case to stop root traversal if we reached a leaf
        if root is None :
            return 0
        
        # Travers left and right
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # +1 to add current depth to recursion
        return max(left, right) + 1
    
# @lc code=end

