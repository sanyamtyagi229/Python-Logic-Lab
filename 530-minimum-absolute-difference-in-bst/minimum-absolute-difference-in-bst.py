class Solution:
    def getMinimumDifference(self, root):

        stack = []
        curr = root

        prev = None
        ans = float('inf')

        while curr or stack:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if prev is not None:
                ans = min(ans, curr.val - prev)

            prev = curr.val

            curr = curr.right

        return ans