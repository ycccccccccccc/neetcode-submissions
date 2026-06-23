# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        if list2.val < list1.val:
            head = list2
            head1 = list1
            head2 = list2.next
        else:
            head = list1
            head1 = list1.next
            head2 = list2
        curr = head

        while curr:
            if not head1:
                curr.next = head2
                return head
            if not head2:
                curr.next = head1
                return head
            if head2.val < head1.val:
                curr.next = head2
                head2 = head2.next
            else:
                curr.next = head1
                head1 = head1.next
            curr = curr.next

        return head