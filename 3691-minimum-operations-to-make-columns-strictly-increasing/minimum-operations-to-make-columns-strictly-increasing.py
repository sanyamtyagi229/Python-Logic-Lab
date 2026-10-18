class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        operations = 0
        
        for j in range(cols):
            for i in range(1, rows):
                if grid[i][j] <= grid[i-1][j]:
                    diff = grid[i-1][j] + 1 - grid[i][j]
                    operations += diff
                    grid[i][j] = grid[i-1][j] + 1
                    
        return operations