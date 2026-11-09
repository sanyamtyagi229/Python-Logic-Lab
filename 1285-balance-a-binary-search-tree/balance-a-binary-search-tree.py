# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        vals = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
            
        inorder(root)
        def build_balanced_bst(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(vals[mid])
            
            node.left = build_balanced_bst(left, mid - 1)
            node.right = build_balanced_bst(mid + 1, right)
            
            return node
            
        return build_balanced_bst(0, len(vals) - 1)