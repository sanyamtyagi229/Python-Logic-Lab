# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        
        def traverse(node):
            if not node:
                return
            result.append(node.val)  # Visit root
            traverse(node.left)      # Traverse left
            traverse(node.right)     # Traverse right
            
        traverse(root)
        return result