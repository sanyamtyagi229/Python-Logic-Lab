class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        x = 0
        blanks = 0
        for char in moves:
            if char == 'L':
                x += 1
            elif char == 'R':
                x -= 1
            else: # char == '_'
                blanks += 1
        return abs(x) + blanks