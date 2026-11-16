class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        frequency_map = {}
        for word in words:
            if word in frequency_map:
                frequency_map[word] += 1
            else:
                frequency_map[word] = 1
        unique_words = []
        for word in frequency_map:
            unique_words.append(word)
        def compare_words(word1, word2):
            freq1 = frequency_map[word1]
            freq2 = frequency_map[word2]
            if freq1 != freq2:
                if freq1 > freq2:
                    return -1
                else:
                    return 1
            else:
                
                if word1 < word2:
                    return -1
                elif word1 > word2:
                    return 1
                else:
                    return 0
        def sorting_key(word):
            frequency = frequency_map[word]
            return (-frequency, word)

        unique_words.sort(key=sorting_key)

        result = []
        for i in range(k):
            result.append(unique_words[i])
            
        return result