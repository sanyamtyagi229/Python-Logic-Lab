class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        # Initialize an array of size 26 to store the minimum frequency for each letter ('a' through 'z')
        # We start by setting it to infinity (or a very large number) for all letters
        min_freq = [float('inf')] * 26
        
        for word in words:
            # Count frequencies for the current word
            current_freq = [0] * 26
            for char in word:
                current_freq[ord(char) - ord('a')] += 1
            for i in range(26):
                min_freq[i] = min(min_freq[i], current_freq[i])
        result = []
        for i in range(26):
            if min_freq[i] > 0 and min_freq[i] != float('inf'):
                # Add the character min_freq[i] times
                result.extend([chr(i + ord('a'))] * min_freq[i])
                
        return result