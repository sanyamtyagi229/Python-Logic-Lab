class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        
        # Directions in clockwise order: East, South, West, North
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        r, c = rStart, cStart
        result.append([r, c])
        
        steps = 1
        d_idx = 0
        
        # We need to collect exactly rows * cols valid cells
        while len(result) < rows * cols:
            # The step length increases by 1 after every two direction changes
            for _ in range(2):
                dr, dc = directions[d_idx]
                
                # Move 'steps' times in the current direction
                for _ in range(steps):
                    r += dr
                    c += dc
                    
                    # Only add to result if the current cell is within grid boundaries
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                        
                # Change to the next direction
                d_idx = (d_idx + 1) % 4
                
            # Increase step size
            steps += 1
            
        return result