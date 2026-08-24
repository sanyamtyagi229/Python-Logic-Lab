class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        
        # Loop through every lowercase letter
        for char in "abcdefghijklmnopqrstuvwxyz":
            # Check if both versions are in the word
            if char in word and char.upper() in word:
                count += 1
                
        return count