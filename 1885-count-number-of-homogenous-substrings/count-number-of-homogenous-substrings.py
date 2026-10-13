class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        current_streak = 0
        prev_char = None
        
        for char in s:
            if char == prev_char:
                current_streak += 1
            else:
                current_streak = 1
                prev_char = char
            total = (total + current_streak) % MOD
            
        return total