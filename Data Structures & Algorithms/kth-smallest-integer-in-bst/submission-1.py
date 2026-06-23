# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        def find_node(node: Optional[TreeNode]):
            nonlocal nums
            if not node: return
            find_node(node.left)
            nums.append(node.val)
            find_node(node.right)
            return

        find_node(root)
        return nums[k-1]
