class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_repeats = (len(b) + len(a) - 1) // len(a)
    
        if b in (a * min_repeats):
            return min_repeats
        if b in (a * (min_repeats + 1)):
            return min_repeats + 1
        if b in (a * (min_repeats + 2)):
            return min_repeats + 2
            
        return -1