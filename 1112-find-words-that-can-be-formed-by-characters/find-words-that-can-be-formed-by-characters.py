class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        # Step 1: Count frequency of each character in chars manually
        chars_count = [0] * 26
        for c in chars:
            chars_count[ord(c) - ord('a')] += 1
            
        total_length = 0
        
        # Step 2: Check each word
        for word in words:
            word_count = [0] * 26
            for c in word:
                word_count[ord(c) - ord('a')] += 1
                
            # Step 3: Verify if word can be formed from chars
            possible = True
            for i in range(26):
                if word_count[i] > chars_count[i]:
                    possible = False
                    break
                    
            if possible:
                total_length += len(word)
                
        return total_length