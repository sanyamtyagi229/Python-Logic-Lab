class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7

        bits = [sum((x >> i) & 1 for x in nums) for i in range(32)]
        ans = 0
        for _ in range(k):
            curr = 0
            for i in range(31, -1, -1):
                if bits[i] > 0:
                    curr |= (1 << i)
                    bits[i] -= 1
            ans = (ans + curr * curr) % MOD
            
        return ans