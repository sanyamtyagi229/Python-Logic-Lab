class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counts = {}
        for char in s:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
                
        for i in range(len(s)):
            if char_counts[s[i]] == 1:
                return i
        return -1
        