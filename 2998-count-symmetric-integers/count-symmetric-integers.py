class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            s = str(i)
            b = len(s)
            if b % 2 != 0:
                continue
            mid = b // 2
            s1 = sum(int(ch) for ch in s[:mid])
            s2 = sum(int(ch) for ch in s[mid:])
            if s1 == s2:
                count += 1
        return count