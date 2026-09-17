class Solution:
    def repeatedCharacter(self, s: str) -> str:
        char_counts = {}
        for char in s:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char]=1
            if char_counts[char]==2:
                return char

                    