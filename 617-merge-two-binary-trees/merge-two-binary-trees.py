
class Solution:
    def mergeTrees(self, root1, root2):

        # Step 1: Pehla tree empty hai
        if root1 is None:
            return root2

        # Step 2: Doosra tree empty hai
        if root2 is None:
            return root1

        # Step 3: Dono nodes ki values add karo
        root1.val = root1.val + root2.val

        # Step 4: Left subtrees merge karo
        root1.left = self.mergeTrees(root1.left, root2.left)

        # Step 5: Right subtrees merge karo
        root1.right = self.mergeTrees(root1.right, root2.right)

        # Step 6: Merged tree return karo
        return root1
