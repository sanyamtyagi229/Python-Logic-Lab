class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        
        # Start at the top-right corner
        row, col = 0, cols - 1
        
        while row < rows and col >= 0:
            current = matrix[row][col]
            
            if current == target:
                return True
            elif current > target:
                # If current is greater, move left to smaller values
                col -= 1
            else:
                # If current is smaller, move down to larger values
                row += 1
                
        return False