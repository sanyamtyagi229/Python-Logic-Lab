from collections import Counter

class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)    
        result = 0
        for word, freq in count1.items():
            if freq == 1 and count2[word] == 1:
                result += 1
                
        return result