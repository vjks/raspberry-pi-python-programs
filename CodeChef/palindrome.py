# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        value = ""
        while head.next != None:
            value += str(head.val)
            head = head.next
            
        if head.next == None:
            value += str(head.val)

        reverse = value[::-1]
        if value == reverse:
            return True
        else:
            return False