class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # 1. Get the binary string (e.g., "101" for 5)
        binary_str = bin(n)[2:]
        
        # 2. Swap the '0's and '1's
        flipped_str = "".join('1' if bit == '0' else '0' for bit in binary_str)
        
        # 3. Convert the flipped binary string back to a base-10 integer
        return int(flipped_str, 2)