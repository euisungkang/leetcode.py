#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int :

        # Make into array so all changes to pointer are updated
        good_nodes = [0]

        def recursiveTraverse(root: TreeNode, max_value: int) :

            # Base Case 
            if root is None :
                return 

            # good node = if current val >= max value so far
            if root.val >= max_value :
                good_nodes[0] += 1
            
            # update max value for deeper recursion
            max_value = max(max_value, root.val)
            
            l = recursiveTraverse(root.left, max_value)
            r = recursiveTraverse(root.right, max_value)
        
        recursiveTraverse(root, float('-inf'))

        return good_nodes[0]


# Original Solution over achieved by returning the list of all
# values of good nodes. Only the # of good nodes is needed.
# Thus no need to return all potential good nodes in any step
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int :

#         # DFS: Returns list of all good nodes
#         def recursiveTraverse(root: TreeNode) -> list :

#             # Base Edge Case: negative inf is lowest number
#             if root is None :
#                 return [float('-inf')]

#             # root node is always (possibly) a good node
#             potential_nodes = [root.val]

#             # recurse left tree and add any good nodes compared to curr
#             left = recursiveTraverse(root.left)
#             for val in left :
#                 if root.val <= val :
#                     potential_nodes.append(val)

#             # recurse right 
#             right = recursiveTraverse(root.right)
#             for val in right :
#                 if root.val <= val :
#                     potential_nodes.append(val)

#             return potential_nodes
        
#         # length of all good nodes = # of good nodes
#         good_nodes = len(recursiveTraverse(root))

#         return good_nodes
        
# @lc code=end

