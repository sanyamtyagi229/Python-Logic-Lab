class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        def helper(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
            
        return helper(0, len(nums) - 1)