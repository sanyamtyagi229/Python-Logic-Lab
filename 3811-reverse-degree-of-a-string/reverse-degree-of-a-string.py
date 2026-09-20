class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        
        for i, char in enumerate(s):
            reversed_val = 123 - ord(char)
            total_degree += reversed_val * (i + 1)
            
        return total_degree