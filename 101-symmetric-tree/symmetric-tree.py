
class Solution:
    def isSymmetric(self, root):

        if root is None:
            return True

        def mirror(left, right):

            # Dono nodes empty hain
            if left is None and right is None:
                return True

            # Sirf ek node empty hai
            if left is None or right is None:
                return False

            # Values different hain
            if left.val != right.val:
                return False

            # Cross-check: left-left with right-right
            outside = mirror(left.left, right.right)

            # Cross-check: left-right with right-left
            inside = mirror(left.right, right.left)

            return outside and inside

        return mirror(root.left, root.right)
