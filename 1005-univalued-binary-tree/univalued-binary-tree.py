class Solution:
    def isUnivalTree(self, root):
        value = root.val

        def check(node):
            if node is None:
                return True

            if node.val != value:
                return False

            a=check(node.left)
            b=check(node.right)
            return a and b

        return check(root)