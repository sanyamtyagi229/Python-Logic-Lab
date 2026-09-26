class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        total_sum = 0
        
        for i in range(n):
            for j in range(n):
                # If the element is on either diagonal, add it
                if i == j or i + j == n - 1:
                    total_sum += mat[i][j]
                    
        return total_sum