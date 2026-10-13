
class Solution:
    def minDepth(self, root):

        # Step 1: Tree empty hai
        if root is None:
            return 0

        # Step 2: Left child missing hai
        if root.left is None:
            return 1 + self.minDepth(root.right)

        # Step 3: Right child missing hai
        if root.right is None:
            return 1 + self.minDepth(root.left)

        # Step 4: Dono children present hain
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return 1 + min(left, right)
