class Solution:
    def searchBST(self, root: TreeNode | None, target: int) -> TreeNode | None:
        if root is None:
            return None
        elif root.val == target:
            return root
        elif root.val < target:
            return self.searchBST(root.right, target)
        else:
            return self.searchBST(root.left, target)