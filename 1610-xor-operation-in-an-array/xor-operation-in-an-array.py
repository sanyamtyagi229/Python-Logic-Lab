class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        k = 0
        for i in range(n):
            k ^= (start + 2 * i)
        return k