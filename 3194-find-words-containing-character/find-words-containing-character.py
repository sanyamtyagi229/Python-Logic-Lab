class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result_indices=[]
        for index, word in enumerate(words):
            if x in word:
                result_indices.append(index)
                
        return result_indices
        