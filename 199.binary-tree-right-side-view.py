#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None :
            return []

        queue = deque([root])
        curr = root
        ans = []

        # Queue will never be empty if we havent finished traversing
        while queue :
            for i in range(len(queue)) :

                # queue = popleft
                curr = queue.popleft()

                
                if curr.left is not None :
                    queue.append(curr.left)
                
                if curr.right is not None :
                    queue.append(curr.right)

            ans.append(curr.val)
            
        return ans
        
# @lc code=end

