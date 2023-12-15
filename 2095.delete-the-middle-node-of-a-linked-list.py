#
# @lc app=leetcode id=2095 lang=python3
#
# [2095] Delete the Middle Node of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None :
            return None

        curr_node = head

        n = 0
        while curr_node is not None :
            n += 1
            curr_node = curr_node.next

        #print(n)


        curr_node = head
        for i in range(n // 2) :
            prev_node = curr_node
            curr_node = curr_node.next
        
        prev_node.next = curr_node.next

        return head
    
# @lc code=end

