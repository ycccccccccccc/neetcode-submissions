# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for i in range(n):
            fast = fast.next
        
        slow = head
        prev = None
        while fast:
            prev = slow
            slow, fast = slow.next, fast.next

        if prev == None:
            return head.next
        if prev.next == None:
            slow.next = None
        else:
            prev.next = prev.next.next
            return head
        