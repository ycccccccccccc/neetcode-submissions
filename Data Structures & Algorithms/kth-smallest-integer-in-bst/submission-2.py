# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums_index, num = 0, 0
        def find_node(node: Optional[TreeNode]):
            nonlocal nums_index, num
            if not node: return
            find_node(node.left)
            nums_index += 1
            if nums_index == k:
                num = node.val
            find_node(node.right)
            return

        find_node(root)
        return num
