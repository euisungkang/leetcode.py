#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # Recursive Function to return leaf value sequence of one tree
        def recursiveTraverse(root: Optional[TreeNode]) -> list :

            # Base Edge Case
            if root is None :
                return []

            # if root is leaf, then return val
            if root.left is None and root.right is None :
                return [root.val]
            
            # Traverse left and right DFS
            l = recursiveTraverse(root.left)
            r = recursiveTraverse(root.right)

            return l + r

        t1 = recursiveTraverse(root1)
        t2 = recursiveTraverse(root2)

        return t1 == t2


# @lc code=end

