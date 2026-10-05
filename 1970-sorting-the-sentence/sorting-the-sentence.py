class Solution:
    def sortSentence(self, s: str) -> str:
        # Split the sentence into individual words
        words = s.split()
        
        # Helper function to extract the trailing digit for sorting
        def extract_index(word):
            return int(word[-1])
        
        # Sort the words using the helper function
        words.sort(key=extract_index)
        
        # Remove the last character (the digit) from each word using a standard for loop
        cleaned_words = []
        for word in words:
            # Slicing to exclude the last character
            original_word = word[:-1]
            cleaned_words.append(original_word)
            
        # Join the words back together with spaces using a standard loop
        result = ""
        for i in range(len(cleaned_words)):
            result += cleaned_words[i]
            if i < len(cleaned_words) - 1:
                result += " "
                
        return result