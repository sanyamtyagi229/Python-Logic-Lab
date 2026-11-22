# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode | None:
        self.i = 0
        n = len(traversal)

        def dfs(depth: int) -> TreeNode | None:
            if self.i >= n:
                return None
            j = self.i
            dashes = 0
            while j < n and traversal[j] == "-":
                dashes += 1
                j += 1
            if dashes != depth:
                return None
            self.i = j
            val = 0
            while self.i < n and traversal[self.i].isdigit():
                val = val * 10 + int(traversal[self.i])
                self.i += 1

            node = TreeNode(val)
            node.left = dfs(depth + 1)
            node.right = dfs(depth + 1)
            return node

        return dfs(0)