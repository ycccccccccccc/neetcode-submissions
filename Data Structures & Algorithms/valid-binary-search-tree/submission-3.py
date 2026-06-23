# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True
        def range_check(node: Optional[TreeNode]) -> (int, int):
            nonlocal valid
            
            if node.left:
                l1, r1 = range_check(node.left)
            else:
                l1, r1 = node.val, node.val-1

            if node.right:
                l2, r2 = range_check(node.right)
            else:
                l2, r2 = node.val+1, node.val

            if node.val <= r1 or node.val >= l2:
                valid = False

            return l1, r2

        range_check(root)
        return valid