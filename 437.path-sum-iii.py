#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int :
        total_paths = [0]

        # DFS: Recursive traversion that returns all possible sums
        def recursiveTraverse(root: Optional[TreeNode]) :
            if root is None :
                return []

            l = recursiveTraverse(root.left)
            r = recursiveTraverse(root.right)

            # current val can be single node path
            if (root.val == targetSum) :
                total_paths[0] += 1

            # Check for any sum paths on all returned child sum of paths
            # Dynamically += curr val for previous traversion
            for i in range(len(l)) :
                l[i] += root.val
                if l[i] == targetSum :
                    total_paths[0] += 1

            # Same for right branch
            for i in range(len(r)) :
                r[i] += root.val
                if r[i] == targetSum :
                    total_paths[0] += 1

            # Return all sum of paths, and current node is a new path
            return l + r + [root.val]
        
        recursiveTraverse(root)

        return total_paths[0]

# @lc code=end

