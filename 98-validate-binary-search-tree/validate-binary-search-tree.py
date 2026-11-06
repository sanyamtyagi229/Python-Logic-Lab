class Solution:
    def isValidBST(self, root):

        def check(node, low, high):

            if node is None:
                return True

            if node.val <= low or node.val >= high:
                return False

            left = check(node.left, low, node.val)

            right = check(node.right, node.val, high)

            return left and right

        return check(root, float('-inf'), float('inf'))