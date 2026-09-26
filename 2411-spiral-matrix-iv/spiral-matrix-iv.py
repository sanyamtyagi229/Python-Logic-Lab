class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode | None) -> list[list[int]]:
        # Initialize the m x n matrix with -1
        matrix = [[-1] * n for _ in range(m)]
        
        # Define the boundaries for our spiral traversal
        top, bottom, left, right = 0, m - 1, 0, n - 1
        curr = head
        
        while curr:
            # Traverse from left to right along the top boundary
            for i in range(left, right + 1):
                if not curr: break
                matrix[top][i] = curr.val
                curr = curr.next
            top += 1
            
            # Traverse from top to bottom along the right boundary
            for i in range(top, bottom + 1):
                if not curr: break
                matrix[i][right] = curr.val
                curr = curr.next
            right -= 1
            
            # Traverse from right to left along the bottom boundary
            for i in range(right, left - 1, -1):
                if not curr: break
                matrix[bottom][i] = curr.val
                curr = curr.next
            bottom -= 1
            
            # Traverse from bottom to top along the left boundary
            for i in range(bottom, top - 1, -1):
                if not curr: break
                matrix[i][left] = curr.val
                curr = curr.next
            left += 1
            
        return matrix