class Solution:
    def checkString(self, s: str) -> bool:
        seen_b = False
        
        for char in s:
            if char == 'b':
                seen_b = True
            elif char == 'a' and seen_b:
                # We found an 'a' after having already seen a 'b'
                return False
                
        return True