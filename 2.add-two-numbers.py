# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def applyCarry(curr, carry) -> Optional[ListNode]:
            if (curr == None and carry == 0):
                return None
            elif (curr == None and carry > 0):
                return ListNode(carry, None)
            else:
                sumValue = curr.val + carry
                if (sumValue >= 10):
                    return ListNode(sumValue % 10, applyCarry(curr.next, sumValue // 10))
                else:
                    curr.val = sumValue
                    return curr

        def traverse(curr1, curr2, carry) -> Optional[ListNode]:
            if (curr1 == None):
                return curr2 if carry == 0 else applyCarry(curr2, carry)
            elif (curr2 == None):
                return curr1 if carry == 0 else applyCarry(curr1, carry)

            sumValue = curr1.val + curr2.val + carry
            if (sumValue >= 10):
                return ListNode(sumValue % 10, traverse(curr1.next, curr2.next, sumValue // 10))
            else:
                return ListNode(sumValue, traverse(curr1.next, curr2.next, 0))

        return traverse(l1, l2, 0)