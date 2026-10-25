class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        seen_frequencies = set()
        for count in freq.values():
            if count in seen_frequencies:
                return False 
            seen_frequencies.add(count)    
        return True