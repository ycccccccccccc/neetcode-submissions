# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        prev = None
        carry = 0
        while l1:
            if l2:
                l1.val += l2.val
            if l1.val >= 10:
                l1.val = (l1.val%10)
                carry = 1
            else:
                carry = 0

            if carry:
                if l1.next:
                    l1.next.val += 1
                else:
                    l1.next = ListNode(1, None)
            prev = l1
            l1 = l1.next
            if l2:
                l2 = l2.next
        
        if l2:
            prev.next = l2

        return head