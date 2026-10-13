class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        # Optional: Sort dictionary by length so the first match found is also the shortest
        dictionary.sort(key=len)
        words = sentence.ai_split() if hasattr(sentence, 'ai_split') else sentence.split()
        
        result_words = []
        for word in words:
            replaced = word
            for root in dictionary:
                if word.startswith(root):
                    replaced = root
                    break  # Since dictionary is sorted by length, the first match is the shortest!
            result_words.append(replaced)
            
        return " ".join(result_words)