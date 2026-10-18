class Solution:
    def isSubtree(self, root, subRoot):

        # Agar subRoot hi empty hai, toh subtree mil gaya
        if subRoot is None:
            return True

        # Agar bada tree empty hai, lekin subRoot empty nahi
        if root is None:
            return False

        # Current node se dono trees same hain?
        if self.isSameTree(root, subRoot):
            return True

        # Nahi, toh left aur right mein search karo
        left_found = self.isSubtree(root.left, subRoot)
        right_found = self.isSubtree(root.right, subRoot)

        return left_found or right_found

    def isSameTree(self, p, q):

        # Dono empty hain
        if p is None and q is None:
            return True

        # Sirf ek empty hai
        if p is None or q is None:
            return False

        # Values different hain
        if p.val != q.val:
            return False

        # Dono ke left aur right bhi same hone chahiye
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return left_same and right_same