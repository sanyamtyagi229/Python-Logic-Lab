class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        c = []
        for i in range(1, n + 1):
            if n % i == 0:
                c.append(nums[i - 1])
                
        squared = [x * x for x in c]
        return sum(squared)