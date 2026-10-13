class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}
        
        # Step 1: Count the frequency of each character in string s
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # Step 2: Iterate through string t and decrement counts
        for char in t:
            if char not in count or count[char] == 0:
                return char
            count[char] -= 1