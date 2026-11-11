# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.stack = []
        # Push all left descendants of the root onto the stack
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node: TreeNode | None):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        # The top of the stack is the next smallest element in the BST
        topest_node = self.stack.pop()
        
        # If the node has a right child, we need to process its left-most descendants
        if topest_node.right:
            self._leftmost_inorder(topest_node.right)
            
        return topest_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()