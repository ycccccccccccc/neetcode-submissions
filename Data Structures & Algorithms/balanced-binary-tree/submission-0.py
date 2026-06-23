# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def get_depth(node: Optional[TreeNode]) -> int:
            nonlocal is_balanced
            if not node: return 0

            left = get_depth(node.left)
            right = get_depth(node.right)

            if abs(left-right) > 1: 
                is_balanced = False
            return max(left, right) + 1

        get_depth(root)
        return is_balanced