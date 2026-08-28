class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        for word in words:
            char_set = set(word.lower())
            if char_set.issubset(row1) or char_set.issubset(row2) or char_set.issubset(row3):
                result.append(word)
                
        return result