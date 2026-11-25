class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n - 2):
            c1 = s[i]
            c2 = s[i + 1]
            c3 = s[i + 2]
            if c1 != c2 and c2 != c3 and c1 != c3:
                count += 1
        return count