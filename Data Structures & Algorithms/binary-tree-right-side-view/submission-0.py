# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        tree = []

        nodes = [(root, 0)]
        while nodes:
            node, level = nodes.pop()
            if not node: continue
            if len(tree) <= level:
                tree.append([])
            tree[level].append(node.val)
            nodes.append((node.right, level+1))
            nodes.append((node.left, level+1))

        print(tree)
        return [tree[i][-1] for i in range(len(tree))]
        