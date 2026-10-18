# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        ls=0
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                ls=root.left.val
            else:
                ls = self.sumOfLeftLeaves(root.left)
        rights=self.sumOfLeftLeaves(root.right)
        return rights+ls
                
        