# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_node = 0
        nodes = [(root, root.val)]
        while nodes:
            node, max_val = nodes.pop()
            if not node: continue
            if node.val >= max_val: 
                good_node += 1
                max_val = node.val
            nodes.extend([(node.left, max_val), (node.right, max_val)])
        return good_node
