class Solution:
    def arrangeWords(self, text: str) -> str:
        words = sorted(text.split(), key=len)
        result = " ".join(words).lower()
        return result[0].upper() + result[1:] if result else ""