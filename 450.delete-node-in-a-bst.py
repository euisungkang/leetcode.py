#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None : 
            return None

        # Traverse tree, and dynamically update respective branch side
        if root.val > key :
            root.left = self.deleteNode(root.left, key)
        elif root.val < key :
            root.right = self.deleteNode(root.right, key)
        
        else :

            # Edge Cases for when node to delete doesnt have 2 children
            if root.left is None :
                return root.right
            if root.right is None :
                return root.left

            # If both children exist, traverse leftmost of right branch
            if root.left and root.right :
                temp = root.right
                while temp.left :
                    temp = temp.left
                root.val = temp.val
            
                # Now that value is changed, go delete the old node
                root.right = self.deleteNode(root.right, root.val)

        return root
        
        
# @lc code=end

