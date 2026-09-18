import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = collections.defaultdict(list)
        
        for word in strs:
            # Sort the characters of the word to form the key
            sorted_word = "".join(sorted(word))
            
            # Append the original word to its anagram group
            anagram_map[sorted_word].append(word)
            
        # Return all the grouped anagrams
        return list(anagram_map.values())