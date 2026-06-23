# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        visit = [root]

        while visit:
            node = visit.pop()
            if not node: continue
            if node.left or node.right:
                temp = node.left
                node.left = node.right
                node.right = temp
                
            visit.append(node.left)
            visit.append(node.right)


        return root
        