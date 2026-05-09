# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
       ans = 0 
       while head:
           ans = ans | head.val
           ans = ans << 1
           head = head.next

       ans = ans >> 1
       return ans
