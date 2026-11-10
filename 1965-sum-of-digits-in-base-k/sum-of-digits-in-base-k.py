class Solution:
    def sumBase(self, n: int, k: int) -> int:
        total_sum = 0
        while n > 0:
            total_sum += n % k
            n //= k
        return total_sum
        