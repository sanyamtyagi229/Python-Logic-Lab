class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = len(matrix)
        
        # Check if every row has exactly 'n' unique numbers
        for row in matrix:
            if len(set(row)) != n:
                return False
        for col in zip(*matrix):
            if len(set(col)) != n:
                return False
                
        return True