class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        n = len(word)
        count = 0
        
        for i in range(n):
            for j in range(i + 4, n):
                sub = word[i:j+1]
                if set(sub) == vowels:
                    count += 1
                    
        return count