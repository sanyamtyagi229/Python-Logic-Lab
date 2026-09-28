class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # Extract the rightmost bit of n
            bit = n & 1
            # Shift res to the left by 1 and add the extracted bit
            res = (res << 1) | bit
            # Shift n to the right by 1 to process the next bit
            n = n >> 1
        return res