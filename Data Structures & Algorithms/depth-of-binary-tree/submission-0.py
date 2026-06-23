# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        visit = [(root, 1)]

        while visit:
            node, depth = visit.pop()
            if not node: continue
            max_depth = max(max_depth, depth)
            
            visit.append((node.left, depth+1))
            visit.append((node.right, depth+1))

        return max_depth