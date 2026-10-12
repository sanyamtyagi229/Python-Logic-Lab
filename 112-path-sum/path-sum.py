
class Solution:
    def hasPathSum(self, root, targetSum):

        if root is None:
            return False

        # Leaf node: no left or right child
        if root.left is None and root.right is None:
            return targetSum == root.val

        remaining = targetSum - root.val

        left_answer = self.hasPathSum(root.left, remaining)
        right_answer = self.hasPathSum(root.right, remaining)

        return left_answer or right_answer
