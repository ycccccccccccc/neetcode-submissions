# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        node = head.next
        last_node = head
        head.next = None
        while node != None:
            print(node.val)
            temp = node.next
            node.next = last_node
            last_node = node
            node = temp
        return last_node